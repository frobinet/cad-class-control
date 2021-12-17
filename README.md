# Connected Autonomous Driving Class - PID Control

This project is based off the Open Source Unity Simulator from Udacity and its Self-Driving Car Nanodegree Capstone Project. Some modifications and customizations have been introduced by us, so don't try to blindly copy existing solutions you might find online.

## Getting Started

- Make sure you have a Python 3 environment installed.
- Install the required python libraries: `pip3 install pandas websockets`
- [Download the simulator for your platform](https://github.com/udacity/self-driving-car-sim/releases/tag/v1.45) and execute it (executable is not signed, proceed anyway)
  - If the file cannot be executed, you may need to make it executable on Linux or MacOS using something like: `chmod +x term2_sim.app/Contents/MacOS/term2_sim_mac`
  - The simulator is not very optimized and consumes a lot of CPU resources, stick to "fastest" quality and low screen resolution at the start.
- We will only be using the "Project 4: PID Controller" environment
- Once the simulator is started, launching `src/main.py` should start moving the car at low speed in a straight line.

## Implementing the controller

- All your control code should lie in `controller.py`. 
  - You should not need to modify `main.py` as it only handles the communication with the simulator. 
  - Your controller should control both the steering and throttle signals.
  - Any command line argument passed to `main.py` will be given to the constructor of your Controller as a string array.
- You are expected to implement at least lateral lateral control (steering angle) control in a the `Controller` class. PID Control is a simple choice, but you may use another controller if you describe it your report. 
- For longitudinal control, you should decide on the target speed by yourself. You should start with a low target speed while implementing lateral control, and then progressively raise it. An ideal solution could set the target speed dynamically based on road curvature in order to maximize speed while staying on course.

## Deliverables

Upload a ZIP file containing your code as well as a short PDF report (max 2 pages)
  - Describe your solution and how you tuned your controller.
  - Plot the cross-track errors over time for different controller tunings and compare them. Is a pure P controller able to succesfully control the car?
  - Analyze the performance of your controller using the CSV log file that main.py outputs.
  - Add a link to a video hosted on any provider (can be non-public as long as it's accessible with the link you share with us). The video should show your best controller successfully completing laps around the track at the highest speed you were able to reach.

