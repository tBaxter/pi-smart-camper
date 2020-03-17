#!/usr/bin/env python3
# This is a fork from the original author, Edoardo Paolo Scalafiotti <edoardo849@gmail.com>
import os
import re
import signal
import sys
import RPi.GPIO as GPIO

from time import sleep


# Per instructions on the fan that came with our Pi, 
# we wired black wire to pin 14 and red wire to pin 2
# Pin 1 is low-power. We did not use it.
pin = 2

# The temperature (in Celsius) at which we trigger the fan
maxTemp = 42

# The temperature (in Celsius) at which we turn the fan off again
minTemp = maxTemp - 1


def setup():
    """
    Gotta do the GPIO things.
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)
    return()

def getCPUtemperature():
    """
    Read (and optionally write) temp
    """
    res = os.popen("vcgencmd measure_temp").readline()
    temp = re.findall(r"\d+\.\d+", res)[0]
    #print("temp is {0}".format(temp)) # Comment/uncomment as needed
    return temp

def setPin(mode): # A little redundant function but useful if you want to add logging
    GPIO.output(pin, mode)
    return()

def fanOn():
    setPin(True)
    return()

def fanOff():
    print("Attempting to turn fan off...")
    setPin(False)
    return()

def getTemp():
    """
    If CPU temp is above max temp, turn it on.
    Don't turn it off until it's below minTemp.
    """
    CPU_temp = float(getCPUtemperature())
    if CPU_temp > maxTemp:
        fanOn()
    elif CPU_temp < minTemp:
        fanOff()
    return()

try:
    setup()
    while True:
        getTemp()
        sleep(5) # Read the temperature every 5 sec
except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup() # resets all GPIO ports used by this program
 