import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  "D:\Python\HACKPSU\\Natural-lang-1-ab3088af655f.json"
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

#takes generated words from the dictionary as one sstring as parameter
def finding_nouns_and_shit(dicti):
    client = language.LanguageServiceClient()
    
    doc = types.Document(content=text_string, type=enums.Document.Type.PLAIN_TEXT)
    nouns_n_shit=client.analyze_syntax(doc).tokens
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    nouns_list = []
    verbs_list = []
    adj_list = []
    for token in nouns_n_shit:
        if (pos_tag[token.part_of_speech.tag]=='NOUN'):
            nouns_list.append(token.text.content)
        if (pos_tag[token.part_of_speech.tag]=='VERB'):
            verbs_list.append(token.text.content)
        if (pos_tag[token.part_of_speech.tag]=='ADJ'):
            adj_list.append(token.text.content)
   
    return nouns_list,verbs_list,adj_list

text_string = 'Docker containers are the future of scalable applications and a must learn skill for any developer. At this workshop you will learn basics of Docker and Software Containers and why they’re important. We will cover setting up Docker, running your first container, creating a basic web application with Python and Docker, and how to publish an application on Docker Hub.'
list1 = finding_nouns_and_shit(text_string)
        
print(list1)
