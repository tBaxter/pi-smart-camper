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

from gpiozero import MotionSensor
from picamera import PiCamera

from settings import PIR_SENSOR_PIN

EMAIL_ADDR = "mail.baxter@gmail.com"
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

def take_photo(cam):
    """
    Take the photo after motion detection
    """
    print("taking photo...")
    img_path = "/var/www/webapp/webcam/%s.jpg" % datetime.now().date()
    cam.capture(img_path)
    print('A photo has been taken')
    sleep(20)

def start_motion_detection():
    """
    Configure and start motion detection.
    """
    print("Motion detection initalizing...")
    pir = MotionSensor(PIR_SENSOR_PIN)
    print("Motion sensor connected on PIN %s" % pir.pin)
    print("Waiting for motion sensor to settle")
    cam = PiCamera()
    cam.resolution = (800, 600)
    pir.when_motion = lambda x: take_photo(cam)
        