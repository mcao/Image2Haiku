import requests

__author__ = 'mrmitty'

DICT_KEY = "ce0f029b4cf8c69b392b134d23582f64"
BASE_URL = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/"
APP_ID = "3637edf1"


def get_phrase(word):
    # we need to add something that will check how many entries are there
    # TODO

    dict_url = BASE_URL + word + "/" + "sentences"
    # print(dict_url)
    req = requests.get(url=dict_url, headers={
                       'app_id': APP_ID, 'app_key': DICT_KEY})
    # print(req.content)
    data = req.json()

    # print(data["results"][0]["lexicalEntries"][0]["sentences"][0]["text"])

    return data["results"][0]["lexicalEntries"][0]["sentences"][0]["text"]
