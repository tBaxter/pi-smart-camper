import datetime
import sys
from threading import Thread

from flask import Flask, render_template, redirect

import RPi.GPIO as GPIO

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
        GPIO.setmode(GPIO.BCM)
        GPIO.remove_event_detect(PIR_SENSOR_PIN)
        GPIO.cleanup()
        cam_thread = None
        message = "Camera is off"
    else:
        message = "I don't know what you want me to do there."
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')