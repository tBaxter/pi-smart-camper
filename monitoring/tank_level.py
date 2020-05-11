import RPi.GPIO as GPIO
import os
import time

from settings import LEVEL_SENSOR_ECHO, LEVEL_SENSOR_TRIGGER

TRIGGER_TIME = 0.00001
MAX_TIME = 0.004  # max time waiting for response in case something is missed

# Define GPIO to use on Pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEVEL_SENSOR_TRIGGER, GPIO.OUT)  # Trigger
GPIO.setup(LEVEL_SENSOR_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Echo
GPIO.output(LEVEL_SENSOR_TRIGGER, False)

def measure():
    """
    This function measures a distance by 
    pulsing the trigger/echo line to initiate a measurement.
    """
    GPIO.output(LEVEL_SENSOR_TRIGGER, True)
    time.sleep(TRIGGER_TIME)
    GPIO.output(LEVEL_SENSOR_TRIGGER, False)

    # ensure start time is set in case of very quick return
    start = time.time()
    timeout = start + MAX_TIME

    # set line to input to check for start of echo response
    while GPIO.input(LEVEL_SENSOR_ECHO) == 0 and start <= timeout:
        start = time.time()

    if(start > timeout):
        return -1

    stop = time.time()
    timeout = stop + MAX_TIME
    # Wait for end of echo response
    while GPIO.input(LEVEL_SENSOR_ECHO) == 1 and stop <= timeout:
        stop = time.time()

    if stop <= timeout:
        elapsed = stop-start
        distance = float(elapsed * 34300)/2.0
    else:
        return -1
    return distance


if __name__ == '__main__':
    try:
        while True:
            distance = measure()
            if(distance > -1):
                print("Measured Distance = %.1f cm" % distance)
            else:
                print("#")
            time.sleep(0.5)
    except KeyboardInterrupt:
        # Reset by pressing CTRL + C
        print("Measurement stopped by User")
        GPIO.cleanup()
