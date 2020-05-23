from os import environ

# API AND SERVICE KEYS
IPINFO_API_KEY = environ.get("IPINFO_API_KEY")
OPENWEATHER_API_KEY = environ.get("OPENWEATHER_API_KEY")

PLEX_USER = environ.get("PLEX_USER")
PLEX_PASS = environ.get("PLEX_PASS")

# GPIO PINS
# Note that these settings are dependent on having a GPIO extension board 
# installed. Otherwise there's just too much IO going on for me
# to keep it all straight.

# PIN Number references are BCM as seen on https://pinout.xyz
# Except in cases where there is no BCM number, in which case 
# They reference the bare pin number, again from https://pinout.xyz.

# Commented out pins are for easy reference. 
# If they're called anywhere, we'll uncomment.

# The power button MUST use pins 5 & 6
#POWER_BUTTON_PIN     = 3     white -> pin 5
#POWER_BUTTON_GROUND  =       green -> pin 6
#POWER_LED_POS        = 14    white -> pin 8 (GPIO14)
#POWER_LED_GROUND     =       red   -> pin 9

#PIR_POWER            =       red    -> pin 2 (5v)
PIR_SENSOR_PIN        = 7   # blue   -> pin 24 (GPIO7)
#PIR_GROUND           =       black  -> pin 25
TEMP_SENSOR           = 4   # purple -> pin 7 (GPIO4)

# Level sensor pin wiring is based mostly on 
# keeping the pins near one another, as seen on 
# https://raspberrypi.stackexchange.com/questions/33955/how-to-use-jsn-sr04t-on-a-raspberry-pi
# LEVEL_SENSOR_POWER = Physical pin 4
# LEVEL_SENSOR_GROUND = Physical pin 6
LEVEL_SENSOR_ECHO = 14 # Green -> pin 8 GPIO 14
LEVEL_SENSOR_TRIGGER = 15 # Blue -> pin 10 GPIO 15
