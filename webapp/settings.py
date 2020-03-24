from os import environ

# Commented out pins are for easy reference. 
# If they're called anywhere, we'll uncomment.
# The power button MUST use pins 5 & 6.
#PIR_POWER            = 4 # (red - 5v pin 4)
#POWER_BUTTON_PIN     = 5 (white)
#POWER_BUTTON_GROUND  = 6 (green)
PIR_SENSOR_PIN        = 7 # (blue - pin 26 - GPIO7 )
#PIR_GROUND           = 25 # (black - ground pin 25)
#POWER_LED_PIN        = 12 (white)
#POWER_LED_GROUND     = 14 (red)

IPINFO_API_KEY = environ.get("IPINFO_API_KEY")
OPENWEATHER_API_KEY = environ.get("OPENWEATHER_API_KEY")

PLEX_USER = environ.get("PLEX_USER")
PLEX_PASS = environ.get("PLEX_PASS")