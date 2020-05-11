import RPi.GPIO as GPIO
import os
import time

from webapp.settings import LEVEL_SENSOR_ECHO, LEVEL_SENSOR_TRIGGER

TRIGGER_TIME = 0.00001
MAX_TIME = 0.004  # max time waiting for response in case something is missed

# Set this to the tank depth in cm
# Our tank is 8.25 inches deep, so we're converting
TANK_DEPTH = round(8.25 * 2.54)
print(TANK_DEPTH)
# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LEVEL_SENSOR_TRIGGER, GPIO.OUT)
GPIO.setup(LEVEL_SENSOR_ECHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(LEVEL_SENSOR_TRIGGER, False)

def measure():
    """
    This function measures a distance by 
    pulsing the trigger/echo line to initiate a measurement.
    """
    #print "Initiating measurement and waiting for sensor to settle..."
    GPIO.output(LEVEL_SENSOR_TRIGGER, False)
    time.sleep(2)
    GPIO.output(LEVEL_SENSOR_TRIGGER, True)
    time.sleep(TRIGGER_TIME)
    GPIO.output(LEVEL_SENSOR_TRIGGER, False)

    # ensure start time is set in case of very quick return
    start = time.time()
    timeout = start + MAX_TIME

    # Start echo
    while GPIO.input(LEVEL_SENSOR_ECHO) == 0:
        start = time.time()

    # Wait for end of echo response
    while GPIO.input(LEVEL_SENSOR_ECHO) == 1:
        stop = time.time()

    pulse_duration = stop-start
    # the speed of sound at sea level is 343m/s or 34300 in CM
    # We want only one-way, so we half it 17150,
    # then round it for cleanliness
    distance = pulse_duration * 17150
    # For convenience, and since I'm 'merican, we'll return it
    # in both cm and inches
    remaining = TANK_DEPTH - distance
    return {
        'cm': round(remaining),
        'in': round(remaining * 0.39,1),
        'full': round(100-((TANK_DEPTH/distance)*100))
    }


if __name__ == '__main__':
    try:
        while True:
            distance = measure()
            if distance:
                print("Measured Distance = %s cm" % distance['cm'])
                print("Measured Distance = %s in" % distance['in'])
                print("Percentage full = %s percent" % distance['full'])
            else:
                print("Unable to measure distance")
            time.sleep(5)
    except KeyboardInterrupt:
        # Reset by pressing CTRL + C
        print("Measurement stopped by User")
        GPIO.cleanup()
