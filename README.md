# Vehicle Steering Script for PiRacer Standard :racing_car:

This Python script allows to control the steering and movement of a vehicle from the command line. It provides various actions such as starting, stopping, turning, and driving forward/backward.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to project directory.
3. (optionall) Create virtual enviroment:
```bash
python3 -m venv venv
source venv/bin/activate 
```
4. Install dependencies:
```bash
pip3 install -r requirements.txt
```
5. Calibrate steering
6. Run the script (look at provided examples)

## Calibration

If the vehicle's wheels are not centered after running the ```python3 steer.py start``` command, you need to adjust the configuration in config.py. Modify the parameters **MAX_RIGHT_PWM_RAW**, **MAX_LEFT_PWM_RAW**, and **NEUTRAL_PWM_RAW** to match requirements.

:information_source: If you don't know much about PWM control, take a look at the links section, they will be helpful for calibration if you are doing it for the first time

## Usage

To use the script, open your terminal and run the following command:
- `<action>`: The action to perform, which can be one of the following:
  - `start`: Start the vehicle.
  - `stop`: Stop the vehicle.
  - `turn_left`: Turn the vehicle left (requires `--value`).
  - `turn_right`: Turn the vehicle right (requires `--value`).
  - `center`: Center the steering.
  - `drive_forward`: Drive the vehicle forward (requires `--value`).
  - `drive_backward`: Drive the vehicle backward (requires `--value`).
- `--value <value>`: This is required for actions that involve turning or driving. ranging from 0 to 100 (min, max). 

## Examples
- Start the vehicle
```bash
python3 steer.py start
```
- Stop the vehicle
```bash
python3 steer.py stop
```
- Turn the vehicle left with a value of 50 (50% range of max turn):
```bash
python3 steer.py turn_left --value 50
```
- Drive the vehicle forward with a speed value of 40 (40% range of max speed):
```bash
python3 steer.py drive_forward --value 40
```

## Tested Enviroment

This script has been tested on the following environment:
- RPi: **Raspberry Pi 4 Model B Rev 1.1**
- OS: **Ubuntu 20.04.5 LTS**
- Kernel: **5.4.0-1069-raspi**

## Useful Links

Here are some useful links for further information on vehicle steering and PWM control:
- [Adafruit **PCA9685** PWM/Servo Shield Usage](https://learn.adafruit.com/adafruit-16-channel-pwm-slash-servo-shield/circuitpython-usage)
- [Useful Tips for Servo Motor **MG996R** Control with Raspberry Pi](https://www.learnrobotics.org/blog/raspberry-pi-servo-motor/)
