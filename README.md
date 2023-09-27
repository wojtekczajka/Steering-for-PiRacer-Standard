# Vehicle Steering Script :racing_car:

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
5. Run the script (look at provided examples)

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