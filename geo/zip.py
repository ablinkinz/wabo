'''
take a zip code and get the geo data
'''
from uszipcode import ZipcodeSearchEngine

def zipToCoord(zipCode):
    search = ZipcodeSearchEngine()
    results = search.by_zipcode(zipCode)
    return results