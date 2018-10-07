import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  "D:\Python\HACKPSU\\Natural-lang-1-ab3088af655f.json"
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import six
import sys


phrase_list = ['Im happy with his performance',
               'I was sad','why are you angry with me?']        
def calculate_average_sentiment_of_emotions(phrase_list):

    client = language_v1.LanguageServiceClient()
    phrase_sentiment_list = []

    for i in range(len(phrase_list)):
    
        type_ = enums.Document.Type.PLAIN_TEXT
        document = {'type': type_, 'content': phrase_list[i]}

        resp = client.analyze_sentiment(document)
        sentiment = resp.document_sentiment
        phrase_sentiment_list.append(sentiment.score)
    return phrase_sentiment_list
    
phrase_sentiment_list = calculate_average_sentiment_of_emotions(phrase_list)
print(phrase_sentiment_list)

    



    
