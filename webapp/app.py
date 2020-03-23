import datetime
import json
import os, re, sys
from threading import Thread

from flask import Flask, render_template, redirect, request

# Because only the Pi has any concept of GPIO 
# the real RPi.GPIO will blow up when trying to test on a Mac.
try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
except ModuleNotFoundError:
    import fake_rpi
    from fake_rpi.RPi import GPIO

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
WEBAPP_DIR = os.path.abspath(os.path.join(PROJECT_DIR, os.path.pardir))
sys.path.append(WEBAPP_DIR)

from settings import PIR_SENSOR_PIN
from modules.weather import get_weather
from monitoring.wifi import get_network_details
from monitoring.motion_sensing import start_motion_detection

# By default these should be off. We'll set later
cam_thread = None
message = None

app = Flask(__name__)

@app.route('/')
def index():
    """
    Pulling together different resources for the main kiosk page.
    Note that a lot of these are just initial values to populate the page.
    We'll have JS update them in real-time.
    
    Where do these come from?
    current_time     - datetime module
    current location - ipinfo/openweather
    weather          - openweather
    camera status    - monitoring/camera
    wifi status      - iw_parse
    # plex?
    # notes
    # battery status?
    # water level?
    # what else?
    """
    global message
    global cam_thread

    cam_status = 'on' if cam_thread else "off"

    weather = get_weather()
    # Strictly debugging:
    try:
        wdata = weather['weather']
    except KeyError:
        print(weather)
        print('key: %s' % os.environ.get("OPENWEATHER_API_KEY"))

    templateData = {
      'message': message,
      'current_time': datetime.datetime.now(),
      'cam_status': cam_status,
      'weather': get_weather(),
      'wifi': get_network_details(),
    }
    return render_template('index.html', **templateData)

@app.route("/status/")
def status():
    """ Output Pi status. """
    global cam_thread

    # can we get power consumption?

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
    try:
        temp = re.findall(r"\d+\.\d+", res)[0]
    except IndexError:
        # since macs don't have vcgencmd, we'll just mock it for testing
        temp = 999

    templateData = {
      'pins' : pins,
      'cpu_temp': temp,
      'cam_thread': cam_thread
    }
    # Pass the template data into the template main.html and return it to the user
    return render_template('status.html', **templateData)


@app.route("/camera/toggle-status/", methods=['GET'])
def camera_action():
    """ Handles turning camera off and on based on user action. """
    global cam_thread
    global message

    if 'cam-status' in request.values:
        # Only do this if we haven't already.
        if not cam_thread:
            cam_thread = Thread(start_motion_detection())
            cam_thread.start()
        message = "Camera is on."
    else:
        # if we didn't explicitly turn it on, then turn it off.
        # also, unchecked checkboxes don't appear to turn up in request.values
        GPIO.setmode(GPIO.BCM)
        GPIO.remove_event_detect(PIR_SENSOR_PIN)
        GPIO.cleanup()
        cam_thread = None
        message = "Camera is off"
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')