import common
import vehicle_config
import vehicle_control

def start_vehicle():
    vehicle_control.start_steering()
    vehicle_control.start_throttle()

def stop_vehicle():
    vehicle_control.stop_throttle()

# turn_value (int): value for turning right from min to max (0 to 100)
def turn_vehicle_right(turn_value: int):
    raw_pwm_cycle_duty = common.map_value(turn_value, 0, 100, vehicle_config.NEUTRAL_PWM_RAW, vehicle_config.MAX_RIGHT_PWM_RAW)
    vehicle_control.set_pwm_duty_cycle_for_steering(raw_pwm_cycle_duty)

# turn_value (int): value for turning left from min to max (0 to 100)
def turn_vehicle_left(turn_value: int):
    raw_pwm_cycle_duty = common.map_value(turn_value, 0, 100, vehicle_config.NEUTRAL_PWM_RAW, vehicle_config.MAX_LEFT_PWM_RAW)
    vehicle_control.set_pwm_duty_cycle_for_steering(raw_pwm_cycle_duty)

def center_steering():
    vehicle_control.set_pwm_duty_cycle_for_steering(vehicle_config.NEUTRAL_PWM_RAW)

# speed_value (int): speed value to driving forward min to max (0 to 100)
def drive_forward(speed_value: int):
    raw_pwm_cycle_duty = common.map_value(speed_value, 0, 100, vehicle_config.PWM_MIN_RAW_VALUE, vehicle_config.PWM_MAX_RAW_VALUE)
    vehicle_control.set_throttle_direction_forward()
    vehicle_control.set_pwm_duty_cycle_for_motors(raw_pwm_cycle_duty)

def set_speed_for_right_motor(speed_value: int):
    raw_pwm_cycle_duty = common.map_value(speed_value, 0, 100, vehicle_config.PWM_MIN_RAW_VALUE, vehicle_config.PWM_MAX_RAW_VALUE)
    vehicle_control.set_throttle_direction_forward()
    vehicle_control.set_pwm_duty_cycle_for_right_motor(raw_pwm_cycle_duty)

def set_speed_for_left_motor(speed_value: int):
    raw_pwm_cycle_duty = common.map_value(speed_value, 0, 100, vehicle_config.PWM_MIN_RAW_VALUE, vehicle_config.PWM_MAX_RAW_VALUE)
    vehicle_control.set_throttle_direction_forward()
    vehicle_control.set_pwm_duty_cycle_for_left_motor(raw_pwm_cycle_duty)

# speed_value (int): speed value to driving backward min to max (0 to 100)
def drive_backward(speed_value: int):
    raw_pwm_cycle_duty = common.map_value(speed_value, 0, 100, vehicle_config.PWM_MIN_RAW_VALUE, vehicle_config.PWM_MAX_RAW_VALUE)
    vehicle_control.set_throttle_direction_backward()
    vehicle_control.set_pwm_duty_cycle_for_motors(raw_pwm_cycle_duty)


    