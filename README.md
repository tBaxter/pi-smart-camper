# pi-smart-camper
The goal is to use a Raspberry Pi to provide some modern-era amenities, monitoring, and "smart-home" niceties to a vintage camper trailer. The camper in question is a 1972 Eco fiberglass egg, 
which is a clone of the [Boler](http://www.boler-camping.com/portfolio/history-of-the-boler/).

I'll keep the code and necessary docs here, but put more general how-to, details and a running progress log on https://www.smartercamper.com.

Here's what's at least tentatively planned:
* Plex, with a decent-size SSD drive to store movies
* Temperature, motion and other sensors to monitor the trailer
* WIFI boosting and cleaning (VPN)
* A cellular modem to send messages if something is out of whack
* An external power button, since the Pi will be hard-wired into the trailer.
* A simple web server so I can monitor things with my phone.

# Setup and Installation
## Pre-requisites

* **[Get an Ipinfo API key](https://ipinfo.io)** so we can geolocate the trailer as you move around. The free plan is more than adequate. 
* **[Get an OpenWeather API key](https://openweathermap.org/)** so we can get the local weather. Again, the free plan is more than adequate. 
* Add your key to `settings.py`. By default, settings will look for the env variable, so you can just `export IPINFO_API_KEY='abc123'` and know you're secure. Feel free to overwrite the settings file as you see fit.
