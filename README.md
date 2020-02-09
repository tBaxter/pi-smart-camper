# pi-smart-camper
The goal is to use a Raspberry Pi to provide some modern-era amenities, monitoring, and "smart-home" niceties to a vintage camper trailer.

The camper in question is a 1972 Eco fiberglass egg, 
which is a clone of the [Boler](http://www.boler-camping.com/portfolio/history-of-the-boler/).

Here's what's at least tentatively planned:
* Plex, with a decent-size SSD drive to store movies
* Temperature, motion and other sensors to monitor the trailer
* WIFI boosting and cleaning (VPN)
* A cellular modem to send messages if something is out of whack
* An external power button, since the Pi will be hard-wired into the trailer.
* A simple web server so I can monitor things with my phone.

## Here's the nuts and bolts:
[12V-5V stepdown converter](https://www.amazon.com/gp/product/B07H7X37T6/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1)
to take the camper's 12V system power down to something Pi-Friendly

[Power button with LED](https://www.amazon.com/gp/product/B07PPDNPW9/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
this is pretty nifty. It's recessed so it won't get toggled accidentally and incorporates an LED so I can see if the PI is on or not. 


## Wiring the power switch
For the power switch, clone the [Pi Power Button repo](https://github.com/Howchoo/pi-power-button) and 
[follow the related instructions](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi). 
Note when you're following the instructions, the files don't have to be written -- they're in the repo. Just use `cp` to move them where you need them and be sure to `chmod` them to set the permissions.
[A simple tutorial](https://howchoo.com/g/ytzjyzy4m2e/build-a-simple-raspberry-pi-led-power-status-indicator) 
took care of the LED portion of the switch. 


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




