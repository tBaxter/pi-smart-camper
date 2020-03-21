import ipinfo
import requests

from webapp.settings import IPINFO_API_KEY, OPENWEATHER_API_KEY

def get_location_data():
    """
    Just a simple, quick call to Ipinfo to see where you're at right now,
    using the official Ipinfo python library.
    Details of what's returned are on https://github.com/ipinfo/python.
    """
    handler = ipinfo.getHandler(IPINFO_API_KEY)
    return handler.getDetails()

def get_weather():
    """
    Get the weather for your current location.

    TO-DO: Consider wrapping the call to get_location_data() so 
    we don't *always* have to get location. Maybe just twice a day?
    How often do we realistically need to check?
    Or can we manually check and then store that?

    There is an unofficial openweather library we could use, but for our 
    simple purposes it doesn't seem necessary. Yet.
    """
    location_data = get_location_data()
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=%s&units=imperial' % (
        location_data.city,
        location_data.region,
        OPENWEATHER_API_KEY
    )
    return requests.get(weather_url).json()




