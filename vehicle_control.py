import busio

from board import SCL, SDA
from adafruit_pca9685 import PCA9685

import vehicle_config

i2c_bus = busio.I2C(SCL, SDA)
steering_pwm_controller = PCA9685(i2c_bus, address=vehicle_config.I2C_STEERING_PWM_CONTROLLER_ADDRESS)
throttle_pwm_controller = PCA9685(i2c_bus, address=vehicle_config.I2C_THROTTLE_PWM_CONTROLLER_ADDRESS)
steering_pwm_controller.frequency = vehicle_config.PWM_FREQ_50HZ
throttle_pwm_controller.frequency = vehicle_config.PWM_FREQ_50HZ

def stop_throttle():
    set_pwm_duty_cycle_for_motors(vehicle_config.PWM_MIN_RAW_VALUE)

def start_steering():
    set_pwm_duty_cycle_on_controller_channel(steering_pwm_controller, vehicle_config.PWM_STEERING_CHANNEL, vehicle_config.NEUTRAL_PWM_RAW)

def start_throttle():
    set_throttle_direction_forward()
    set_pwm_duty_cycle_for_motors(vehicle_config.PWM_MIN_RAW_VALUE)

def set_throttle_direction_forward():
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN1].duty_cycle = vehicle_config.PWM_MAX_RAW_VALUE
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN2].duty_cycle = vehicle_config.PWM_MIN_RAW_VALUE
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN1].duty_cycle = vehicle_config.PWM_MIN_RAW_VALUE
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN2].duty_cycle = vehicle_config.PWM_MAX_RAW_VALUE

def set_throttle_direction_backward():
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN1].duty_cycle = vehicle_config.PWM_MIN_RAW_VALUE
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN2].duty_cycle = vehicle_config.PWM_MAX_RAW_VALUE
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN1].duty_cycle = vehicle_config.PWM_MAX_RAW_VALUE
    throttle_pwm_controller.channels[vehicle_config.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN2].duty_cycle = vehicle_config.PWM_MIN_RAW_VALUE

def set_pwm_duty_cycle_for_steering(pwm_duty_cycle: int):
    validate_pwm_cycle_duty_for_steering(pwm_duty_cycle)
    print
    set_pwm_duty_cycle_on_controller_channel(steering_pwm_controller, vehicle_config.PWM_STEERING_CHANNEL, pwm_duty_cycle)

def validate_pwm_cycle_duty_for_steering(pwm_cycle_duty: int):
    if not (vehicle_config.MAX_LEFT_PWM_RAW <= pwm_cycle_duty <= vehicle_config.MAX_RIGHT_PWM_RAW):
        raise ValueError(f"PWM RAW CYCLE DUTY value for steering should be between {vehicle_config.MAX_LEFT_PWM_RAW} and {vehicle_config.MAX_RIGHT_PWM_RAW}.")
    
def set_pwm_duty_cycle_for_motors(pwm_duty_cycle: int):
    validate_pwm_cycle_duty_for_motors(pwm_duty_cycle)
    set_pwm_duty_cycle_on_controller_channel(throttle_pwm_controller, vehicle_config.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_PWM, pwm_duty_cycle)
    set_pwm_duty_cycle_on_controller_channel(throttle_pwm_controller, vehicle_config.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_PWM, pwm_duty_cycle)

def set_pwm_duty_cycle_for_left_motor(pwm_duty_cycle: int):
    validate_pwm_cycle_duty_for_motors(pwm_duty_cycle)
    set_pwm_duty_cycle_on_controller_channel(throttle_pwm_controller, vehicle_config.PWM_THROTTLE_CHANNEL_LEFT_MOTOR_PWM, pwm_duty_cycle)

def set_pwm_duty_cycle_for_right_motor(pwm_duty_cycle: int):
    validate_pwm_cycle_duty_for_motors(pwm_duty_cycle)
    set_pwm_duty_cycle_on_controller_channel(throttle_pwm_controller, vehicle_config.PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_PWM, pwm_duty_cycle)

def validate_pwm_cycle_duty_for_motors(pwm_cycle_duty: int):
    if not (vehicle_config.PWM_MIN_RAW_VALUE <= pwm_cycle_duty <= vehicle_config.PWM_MAX_RAW_VALUE):
        raise ValueError(f"PWM RAW CYCLE DUTY value for motors should be between {vehicle_config.PWM_MIN_RAW_VALUE} and {vehicle_config.PWM_MAX_RAW_VALUE}.")
    
def set_pwm_duty_cycle_on_controller_channel(controller: PCA9685, channel: int, pwm_duty_cycle: int):
    controller.channels[channel].duty_cycle = pwm_duty_cycle



