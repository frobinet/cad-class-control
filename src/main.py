#!/usr/bin/env python3

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("control")

import asyncio
import websockets
import json
import pandas as pd
from controller import Controller
from pathlib import Path
import sys
from typing import Dict, Any


def create_message(steering_signal: float, throttle_signal: float):
    assert -1 <= steering_signal <= 1, f"Invalid steering signal {steering_signal} not in [-1,1]"
    assert -1 <= throttle_signal <= 1, f"Invalid throttle signal {throttle_signal} not in [-1,1]"
    msg_json = {"steering_angle": steering_signal, "throttle": throttle_signal}
    msg = f'42["steer",{json.dumps(msg_json)}]'
    return msg

def find_new_log_path() -> Path:
    index = 0
    while True:
        log_path = Path(f'logs{index}.csv')
        if not log_path.exists():
            break
        else:
            index += 1
    return log_path

def write_csv(path: Path, data: Dict[str, Any]):
    df = pd.DataFrame([data])
    include_header = not path.exists()
    df.to_csv(path, mode="a", header=include_header, index=False)

async def echo(websocket):
    csv_path = find_new_log_path()
    logger.info(f"New connection: inputs/outputs will be logged to {csv_path}")
    controller = Controller(sys.argv)
    async for str_message in websocket:
        if str_message.startswith("42"): # Sim protocol uses 42 before json messages
            [msg_type, msg] = json.loads(str_message[2:])
            if msg_type != "telemetry":
                logger.warning(f"Received unknown message: {str_message}")
            else:
                # Compute new control signals and send response
                del msg["image"] # We don't need the raw image
                steering_angle, throttle, speed, cross_track_error = [float(msg[k]) for k in ["steering_angle", "throttle", "speed", "cte"]]
                steering_signal, throttle_signal = controller.compute_new_control(steering_angle, throttle, speed, cross_track_error)
                response = create_message(steering_signal, throttle_signal)
                # Log data to csv for analysis
                csv_data = {**msg, "steering_signal": steering_signal, "throttle_signal": throttle_signal}
                write_csv(csv_path, csv_data)
                await websocket.send(response)
        else:
            logger.warning(f"Ignoring unknown message: {str_message}")

async def main():
    host = "localhost"
    port = 4567
    async with websockets.serve(echo, host, port):
        logger.info(f"Listening for clients on ws://{host}:{port}")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
