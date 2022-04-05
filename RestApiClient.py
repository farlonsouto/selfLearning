import json
import urllib.request


class RestApiClient:
    """ Abstracts a simple REST API Client for learning purposes"""

    def __init__(self, url):
        self.url = url

    def getData(self):
        """ Performs a call to the API, reads the content and retrieves it in JSON format"""
        resp = urllib.request.urlopen(self.url)
        return resp.read().decode("utf-8")


satelliteId = input("Inform the satellite ID:")
# Simple case where we are always looking for the ISS - International Space Station
client = RestApiClient("https://api.wheretheiss.at/v1/satellites/{}".format(satelliteId))
dictionaryFromJson = json.loads(client.getData())
print("Information collected: {}".format(dictionaryFromJson))