import requests

__author__ = 'mrmitty'

###############################################
#Name of File: dictionary.py
#Purpose of File:
#API’s: Oxford Dictionary
###############################################

DICT_KEY = "ce0f029b4cf8c69b392b134d23582f64"
BASE_URL = "https://od-api.oxforddictionaries.com:443/api/v1/entries/en/"
APP_ID = "3637edf1"

###############################################
#Precondition: String of a word
#Postcondition: Returns one phrase of how the word is sused
#Summary: Accesses Oxford Dictionary to retrieve a phrase of a word
###############################################
def get_phrase(word):
    # we need to add something that will check how many entries are there

    dict_url = BASE_URL + word + "/" + "sentences"
    # print(dict_url)
    req = requests.get(url=dict_url, headers={'app_id': APP_ID, 'app_key': DICT_KEY})
    data = req.json()

    # print(data["results"][0]["lexicalEntries"][0]["sentences"][0]["text"])

    return data["results"][0]["lexicalEntries"][0]["sentences"][0]["text"]

###############################################
#Precondition: List of multiple words, or just one word, list or string doesnt matter
#Postcondition: Returns a list of synonyms
#Summary: Sends words to Oxford and gets 4 synonyms for each word
###############################################
def get_syn(word):
    if (len(word) == 0):
        return "none";
    #returns if nothing is given
    
    if (len(word[0]) == 1)):
        #this is just one word as a string
        length = 1
    else:
        #This is more than one word, or it could be one word in a list
        length = len(word)
    

    synonyms = []
    for x in range(0, length):
        dict_url = BASE_URL + word[x] + "/synonyms"
        req = requests.get(url=dict_url, headers={'Accept': "application/json", 'app_id': APP_ID, 'app_key': DICT_KEY})

        try:
            data = req.json()

            temp = word[x]
            for y in range(0, 4):
                temp = temp + " " + (data["results"][0]["lexicalEntries"][0]["entries"]
                                     [0]["senses"][0]["subsenses"][1]["synonyms"][y]["text"])
            synonyms.append(temp)
        except:
            continue

    res = ''
    for lst in synonyms:
        res += lst + ' '

    return res
