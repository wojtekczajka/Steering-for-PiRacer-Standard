import RPi.GPIO as GPIO
import time

class DistanceSensor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.PIN_TRIGGER = 4
        self.PIN_ECHO = 17
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
        print("Waiting for sensor to settle")
        time.sleep(2)

    def measure_distance(self):
        GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(self.PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(self.PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        return distance

    def cleanup(self):
        GPIO.cleanup()

    def __del__(self):
        self.cleanup()


# Usage:
# sensor = DistanceSensor()
# distance = sensor.measure_distance()
# print(f"Distance: {distance} cm")
# distance = sensor.measure_distance()
# print(f"Distance: {distance} cm")
