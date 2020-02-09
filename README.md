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

### Here's the nuts and bolts:
[12V-5V stepdown converter](https://www.amazon.com/gp/product/B07H7X37T6/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1)
to take the camper's 12V system power down to something Pi-Friendly

[Power button with LED](https://www.amazon.com/gp/product/B07PPDNPW9/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
this is pretty nifty. It's recessed so it won't get toggled accidentally and incorporates an LED so I can see if the PI is on or not. 


### Wiring the power switch
For the power switch, clone the [Pi Power Button repo](https://github.com/Howchoo/pi-power-button) and 
[follow the related instructions](https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi). 
[A simple tutorial](https://howchoo.com/g/ytzjyzy4m2e/build-a-simple-raspberry-pi-led-power-status-indicator) 
took care of the LED portion of the switch.

