import json
import requests

from riotwatcher import LolWatcher, ApiError

class Api:
    def __init__(self):
        with open('API_keyjson') as f:
            self.api_key = json.load(f)

        self.lolwatcher = LolWatcher(self.api_key)

    def get(self, url):
        try:
            return requests.get(url+self.api_key)
        except ApiError as err:
            message = 'response:'+str(err.response.status_code)
            if err.response.status_code == 429:
                print(message, 'Probably too many requests.')
            elif err.response.status_code == 404:
                print(message, 'Not found.')
            elif err.response.status_code == 403:
                print(message, 'Probably bad API key.')
                key = input('Input new key:')
                with open('API_key.json', 'w') as f:
                    json.dump(key, f)



    def getSummonerId(self, name):
        self.get(fr"https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?")
