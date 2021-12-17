from typing import List

# TODO All your code should go here. You should not need to modify main.py
class Controller:
    def __init__(self, command_line_args: List[str]):
        # command_line_args given to main.py are passed here to allow you to vary the behaviour
        # of your controller depending on them (eg. test different values for PID parameters without touching the code)
        pass

    def compute_new_control(self, steering_angle: float, throttle: float, speed: float, cross_track_error: float):
        # Dummy controller that drives straight with constant throttle
        steering_signal = 0.0 # Has to be in [-1,1]
        throttle_signal = 0.3 # Also in [-1,1] (negative values for braking/reverse)
        return steering_signal, throttle_signal
