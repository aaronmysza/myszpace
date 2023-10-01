import requests
import json


class SetlistFmApiRepo():
    def __init__(self):
        self.url = "https://api.setlist.fm/rest/1.0"
        self.headers = {
            "x-api-key": "dXebbZafqdHjqJL8qWk1RY5GMychmw_mrPvX",
            "Accept": 'application/json'
        }

    def call_api(self, endpoint_url, params):
        response = requests.request("GET", endpoint_url, headers=self.headers, params=params)
        response_json = json.loads(response.text)
        print(response_json)
        return response_json
