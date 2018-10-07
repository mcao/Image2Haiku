import requests

__author__ = 'mrmitty'

DICT_KEY = "ce0f029b4cf8c69b392b134d23582f64"
BASE_URL = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/"
APP_ID = "3637edf1"


def get_phrase(word):
    # we need to add something that will check how many entries are there

    dict_url = BASE_URL + word + "/" + "sentences"
    # print(dict_url)
    req = requests.get(url=dict_url, headers={
                       'app_id': APP_ID, 'app_key': DICT_KEY})
    data = req.json()

    # print(data["results"][0]["lexicalEntries"][0]["sentences"][0]["text"])

    return data["results"][0]["lexicalEntries"][0]["sentences"][0]["text"]


def get_syn(word):
    length = len(word)

    synonyms = []
    for x in range(0, length):
        dict_url = BASE_URL + word[x] + "/synonyms"
        req = requests.get(url=dict_url, headers={
                           'Accept': "application/json", 'app_id': APP_ID, 'app_key': DICT_KEY})

        try:
            data = req.json()

            temp = word[x]
            for y in range(0, 4):
                temp = temp + " " + (data["results"][0]["lexicalEntries"][0]["entries"]
                                     [0]["senses"][0]["subsenses"][1]["synonyms"][y]["text"])
            synonyms.append(temp)
        except:
            continue

    # print(data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"][0]["text"])
    #list = word +" " + data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"][0]["text"] + " " + data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"][1]["text"] + " " + data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"][2]["text"] + " " + data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"][3]["text"] + " " + data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"][1]["synonyms"][4]["text"]

    # print(list[1])

    res = ''
    for lst in synonyms:
        res += lst + ' '

    return res
