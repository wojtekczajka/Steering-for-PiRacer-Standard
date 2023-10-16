from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ultrasonic_hcsr04 import DistanceSensor
import vehicle_steering

app = FastAPI()

distance_sensor = DistanceSensor()

class Action(BaseModel):
    action: str
    value: int = None

@app.post("/control/")
async def control_vehicle(action_data: Action):
    action = action_data.action
    value = action_data.value

    if value is not None and not (0 <= value <= 100):
        raise HTTPException(status_code=400, detail="Value must be in the range 0 to 100")

    if action == "start":
        vehicle_steering.start_vehicle()
    elif action == "stop":
        vehicle_steering.stop_vehicle()
    elif action == "turn_left" and value is not None:
        vehicle_steering.turn_vehicle_left(value)
    elif action == "turn_right" and value is not None:
        vehicle_steering.turn_vehicle_right(value)
    elif action == "center":
        vehicle_steering.center_steering()
    elif action == "drive_forward" and value is not None:
        # vehicle_steering.set_speed_for_left_motor(value)
        vehicle_steering.drive_forward(value)
    elif action == "drive_backward" and value is not None:
        vehicle_steering.drive_backward(value)
    elif action == "set_speed_for_right_motor" and value is not None:
        vehicle_steering.set_speed_for_right_motor(value)
    elif action == "set_speed_for_left_motor" and value is not None:
        vehicle_steering.set_speed_for_left_motor(value)
    else:
        raise HTTPException(status_code=400, detail="Invalid action or missing value")

    return {"message": "Action performed successfully"}

@app.get("/get_distance/")
async def get_distance():
    distance = distance_sensor.measure_distance()
    return {"distance": distance}
