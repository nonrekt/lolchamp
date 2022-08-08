import json
from riotwatcher import LolWatcher, ApiError

class Login:
    def __init__(self):
        with open('API_keyjson') as f:
            self.API_KEY = json.load(f)

        self.lolwatcher = LolWatcher(self.API_KEY)
