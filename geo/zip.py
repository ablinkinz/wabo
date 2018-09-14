'''
take a zip code and get the geo data
'''
from uszipcode import ZipcodeSearchEngine
import requests
import json


def zipToCoord(zipCode):
    """
    take zip code and convert them to a zip code
    :param zipCode:
    :return:
    """
    search = ZipcodeSearchEngine()
    results = search.by_zipcode(zipCode)
    return results


def zipFromCityState(city, state):
    """

    :param city:
    :param state:
    :return:
    """
    search = ZipcodeSearchEngine()
    return search.by_city_and_state(city, state)


def getZipCode():
    """

    :return:
    """
    url = 'http://ipinfo.io/json'
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    data = response.json()
    IP = data['ip']
    org = data['org']
    city = data['city']
    country = data['country']
    region = data['region']
    results = zipFromCityState(city, region)
    zipcode = results[0]["Zipcode"]
    return zipcode


def getState():
    """

    :return:
    """
    url = 'http://ipinfo.io/json'
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    data = response.json()
    state = data['region']
    return state


def getCoord():
    """

    :return:
    """
    url = 'http://ipinfo.io/json'
    response = requests.get(url, headers={'User-agent': 'Mozilla/5.0'})
    data = response.json()
    coord = data['loc']
    return coord
