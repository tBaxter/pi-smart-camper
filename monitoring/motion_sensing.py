import smtplib, ssl
from datetime import datetime
from time import sleep
from threading import Thread

# Imports to allow us to email. 
# We may not need this in the future.
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

import RPi.GPIO as GPIO
from picamera import PiCamera

EMAIL_ADDR: = "mail.baxter@gmail.com"
EMAIL_SUBJECT = "Motion detected by RPi"


def send_email(img_path):
    """
    Should send an email, when properly configured with an SMTP server.
    May not be needed if we can get modem working correctly.
    """
    msg = MIMEMultipart()
    msg['Subject'] = EMAIL_SUBJECT
    msg['To'] = EMAIL_ADDR
    msg['From'] = EMAIL_ADDR
    msg.preamble ="Message sent from RPi "
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(img_path, 'rb').read())
    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        'attachment; filename="motion_pic.jpg"'
    )
    msg.attach(part)
    # to do: figure this bit out in a way that's
    # sharable and reusable
    try:
        s =smtplib.SMTP('some smtp server', 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        
        s.login(
            user = 'smtp service user',
            password = 'smtp service pass'
        )
        s.sendmail(email_addr, email_addr, msg.as_string())
        s.quit()
    except Exception as error:
        # To do: log this error
        print("Error: %s" % error)

def motion_callback(cam):
    """
    Just create and store an image, using the time as filename,
    then send it out.
    """
    img_path = "/home/pi/camphotos/%s.jpg" % datetime.now().date()
    cam.capture(img_path)
    send_email(img_path)

def start_camera():
    """
    Configure and start the camera up on demand.
    """
    SENSOR_PIN = 7
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    cam = PiCamera()
    cam.resolution = (800, 600)
    img_path = "/home/pi/camphotos/%s.jpg" % datetime.now().date()
    print("Motion detection initalizing...")
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=lambda x: motion_callback(cam))
