'''
Programme that makes http request to the API 
and gets data about events in Helsinki
'''
import urllib.request
import json


def search_events():
    with urllib.request.urlopen('https://open-api.myhelsinki.fi/v1/events/') as response:
        data = response.read()

    events = json.loads(data)
    return events['data']
