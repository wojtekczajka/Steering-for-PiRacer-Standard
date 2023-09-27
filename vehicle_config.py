PWM_RESOLUTION = 16
PWM_MAX_RAW_VALUE = 2**PWM_RESOLUTION - 1
PWM_MIN_RAW_VALUE = 0
PWM_FREQ_50HZ = 50.0
PWM_WAVELENGTH_50HZ = 1.0 / PWM_FREQ_50HZ

PWM_STEERING_CHANNEL = 0
I2C_STEERING_PWM_CONTROLLER_ADDRESS = 0x40
MAX_RIGHT_PWM_RAW = 5500
MAX_LEFT_PWM_RAW = 2500
NEUTRAL_PWM_RAW = 4000

PWM_THROTTLE_CHANNEL = 1
I2C_THROTTLE_PWM_CONTROLLER_ADDRESS = 0x60
PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN1 = 5
PWM_THROTTLE_CHANNEL_LEFT_MOTOR_IN2 = 6
PWM_THROTTLE_CHANNEL_LEFT_MOTOR_PWM = 7
PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN1 = 1
PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_IN2 = 2
PWM_THROTTLE_CHANNEL_RIGHT_MOTOR_PWM = 0