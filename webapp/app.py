import datetime
import os, re, sys
from threading import Thread

from flask import Flask, render_template, redirect

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
sys.path.append('../')

from settings import PIR_SENSOR_PIN
from monitoring.motion_sensing import start_motion_detection

# By default these should be off. We'll set later
cam_thread = None
message = None

app = Flask(__name__)

@app.route('/')
def index():
   global cam_thread
   global message

   templateData = {
      'title' : 'HELLO!',
      'message': message,
      'cam_thread': cam_thread
   }
   return render_template('index.html', **templateData)

@app.route("/camera/<action>")
def action(action):
    """ Handles turning camera off and on based on user action. """
    global cam_thread
    global message

    if action == "on":
        # Only do this if we haven't already.
        if not cam_thread:
            cam_thread = Thread(start_motion_detection())
            cam_thread.start()
        message = "Camera is on."
    elif action == "off":
        GPIO.remove_event_detect(PIR_SENSOR_PIN)
        GPIO.cleanup()
        cam_thread = None
        message = "Camera is off"
    else:
        message = "I don't know what you want me to do there."
    return redirect("/")

@app.route("/status/")
def status(action):
    """ Output Pi status. """
    # Create a dictionary called pins to store the pin number, name, and pin state:
    pins = {
        3 : {'name' : 'Power button', 'state' : GPIO.LOW, 'physical pin': 5},
        7 : {'name' : 'PIR SENSOR', 'state' : GPIO.LOW, 'phsyical pin': 26},
        12 : {'name' : 'Power LED', 'state' : GPIO.LOW, 'physical pin': 12}
    }
    for pin in pins:
        # For each pin, read the pin state and store it in the pins dictionary:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
        pins[pin]['state'] = GPIO.input(pin)
    # get cpu temp
    res = os.popen("vcgencmd measure_temp").readline()
    temp = re.findall(r"\d+\.\d+", res)[0]

    templateData = {
      'pins' : pins,
      'cpu_temp': temp
    }
    # Pass the template data into the template main.html and return it to the user
    return render_template('status.html', **templateData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')