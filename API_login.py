import json


class Login:
    def __init__(self):
        with open('API_key.json') as f:
            self.API_KEY = json.load(f)

        self.lolwatcher = LolWatcher(API_KEY)
