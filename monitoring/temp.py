#!/usr/bin/python
import glob
import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT) 

#from gpiozero import Buzzer
#buzzer = Buzzer(24)

# Wiring:
# Power: 3.3 or 5. Either is fine.
# Ground : Pin 6 is easiest
# Data: BCM 4 (pin 7) is best 
# Buzzer In : 24

# Get your sensor. If this fails, your device probably isn't wired up right.
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    """
    Simply read all output from the sensor
    """
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    """
    Return usable version of raw temp, in celsius and farhenheit.
    """
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        if temp_f >= 77.0:
            print("It's gettin' hot in here...")
            #buzzer.beep()
            sleep(0.5)
        #buzzer.off()
        return temp_c, temp_f

while True:
    print(read_temp())
    time.sleep(1)
