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
* Add your key to `settings.py`. By default, settings will look for the env variable, so you can just `export IPINFO_API_KEY='abc123'` and know you're secure, but feel free to overwrite the settings file as you see fit.


## The cellular modem
This is a giant pain, and I still don't know if I can actually get it to work or not.
[The USB modem I purchased](https://www.amazon.com/gp/product/B07X129SNS/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) took six weeks to arrive and came with almost no instructions. It took awhile to even figure out where to put the SIM card. Definitely not recommended. But it's what I have, and it _should_ work. I've copied the Linux instructions found on the modem itself here, but so far I don't trust them. We'll see.

The instructions are hard to find because by default the modem doesn't want to mount on the Pi, and it doesn't appear as a USB drive, either. So that's fun. 


## Monitoring
### External temperature: _to come_
### Motion detection: _to come_
### Smoke detection: _to come_

### Internal temperature monitoring
Given a lack of ventilation, I have some concerns about CPU temp. The `internal-temp.py` script will allow me to monitor it and if I see it get high, I can easily add a fan for extra cooling when the temp climbs.

To-Do: have it run automatically in the background.




