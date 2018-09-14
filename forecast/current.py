"""
get current weather from openweathermap
http://api.openweathermap.org/data/2.5/weather?zip=29483,us&units=imperial&APPID=dac78dd6b65aa85c4c2499d9872984db
"""

import urllib
import json
import config
import requests


class GetOpenWeatherCurrentWeather:
    """
    if you want to import and call this in your own script you could call this like
    this is currently not used 2018.09.14
    >>> currentConditions = getCurrentWeather()
    >>> cityName = currentConditions.results()["name"]
    >>> print(cityName)
    Charleston
    """
    def __init__(self):
        self.settings = config.getSettings()
        self.weatherAPIKey = self.settings["openWeatherMapAPIKey"]
        self.zipCode = self.settings["zipCode"]
        self.units = self.settings["units"]

    def results(self):
        url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,us&units=%s&APPID=%s" % (self.zipCode, self.units, self.weatherAPIKey)
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        return data


class GetWeatherDotGovAlerts:
    """
    get severe weather alerts from weather.gov
    https://api.weather.gov/alerts/active?status=actual&message_type=alert&area=SC
    """

    def __init__(self):
        self.settings = config.getSettings()
        self.state = self.settings["state"]
        if self.state == "":
            self.coord = self.settings["coord"]
            if self.coord == "":
                import geo
                self.coord = geo.getCoord()

    def results(self):
        if self.coord:
            url = "https://api.weather.gov/alerts/active?status=actual&message_type=alert&point=%s" % self.coord
        else:
            url = "https://api.weather.gov/alerts/active?status=actual&message_type=alert&area=%s" % self.state
        response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
        jsonResults = response.json()
        return jsonResults



