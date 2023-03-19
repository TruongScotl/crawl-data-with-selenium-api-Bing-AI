import googlemaps
from utils import read_key

key = read_key('files/geocoding_api.txt')

gmaps = googlemaps.Client(key=key)

def geocode(andress)->dict:

    """
    Input: string of andress
    Return: dict {"lat":......, "lng":.......}
    """
    geocode = gmaps.geocode(andress)
    result = geocode[0]["geometry"]["location"]
    return result
