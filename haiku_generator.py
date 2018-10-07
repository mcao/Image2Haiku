import random
import os
from google import cloud
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import dictionary

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./Natural-lang-1-ab3088af655f.json"


def find_adjectives(dicti):
    client = language.LanguageServiceClient()

    doc = types.Document(content=dicti, type=enums.Document.Type.PLAIN_TEXT)
    nouns_n_shit = client.analyze_syntax(doc).tokens
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    adj = []
    for token in nouns_n_shit:
        if (pos_tag[token.part_of_speech.tag] == 'ADJ'):
            adj.append(token.text.content)

    return adj


def find_nouns(dicti):
    client = language.LanguageServiceClient()

    doc = types.Document(content=dicti, type=enums.Document.Type.PLAIN_TEXT)
    nouns_n_shit = client.analyze_syntax(doc).tokens
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    noun = []
    for token in nouns_n_shit:
        if (pos_tag[token.part_of_speech.tag] == 'NOUN'):
            noun.append(token.text.content)

    return noun


def find_verbs(dicti):
    client = language.LanguageServiceClient()

    doc = types.Document(content=dicti, type=enums.Document.Type.PLAIN_TEXT)
    nouns_n_shit = client.analyze_syntax(doc).tokens
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')
    verb = []
    for token in nouns_n_shit:
        if (pos_tag[token.part_of_speech.tag] == 'VERB'):
            verb.append(token.text.content)

    return verb

# https://stackoverflow.com/questions/46759492/syllable-count-in-python


def syllable_count(some_list):
    syllable_list = []

    for i in range(len(some_list)):
        some_list[i] = some_list[i].lower()

        word = some_list[i]
        count = 0
        vowels = "aeiouy"

        if word[0] in vowels:
            count += 1

        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
                if word.endswith("e"):
                    count -= 1

        if count == 0:
            count += 1

        syllable_list.append(count)

    return syllable_list


def adj_to_adj_lst(adj):
    adj_lst = [adj, syllable_count(adj)]
    return adj_lst


def noun_to_noun_lst(noun):
    noun_lst = [noun, syllable_count(noun)]
    return noun_lst


def verb_to_verb_lst(verb):
    verb_lst = [verb, syllable_count(verb)]
    return verb_lst


def adj_lst_to_dict(adj_lst):
    adj_dict = {}
    for i in range(len(adj_lst)):
        adj_dict[adj_lst[0][i]] = adj_lst[1][i]

    return adj_dict


def noun_lst_to_dict(noun_lst):  # , noun_lst, verb_lst):
    noun_dict = {}
    for i in range(len(noun_lst)):
        noun_dict[noun_lst[0][i]] = noun_lst[1][i]

    return noun_dict


def verb_lst_to_dict(verb_lst):  # , noun_lst, verb_lst):
    verb_dict = {}
    for i in range(len(verb_lst)):
        verb_dict[verb_lst[0][i]] = verb_lst[1][i]

    return verb_dict


def first_line_generator(adj_dict, noun_dict, verb_dict):
    # first line
    syllable = 0
    tries = 0
    first = False
    possible_firsts = {}

    while first == False:
        if tries == len(adj_dict) or tries == len(noun_dict) or tries == len(verb_dict):
            # sort by value
            sorted_by_value = sorted(
                possible_firsts.items(), key=lambda kv: kv[1], reverse=True)
            for key in sorted_by_value:
                if (key[1]) > 5:
                    continue
                else:
                    first_line = key
                    return first_line[0]

        adj,  adj_syllables = random.choice(list(adj_dict.items()))
        noun, noun_syllables = random.choice(list(noun_dict.items()))
        verb, verb_syllables = random.choice(list(verb_dict.items()))

        # create a dictionary of the adj+noun+verb : total_syllables
        syllable = noun_syllables + adj_syllables + verb_syllables
        first_line = '{} {} {}'.format(adj, noun, verb)
        possible_firsts[first_line] = syllable

        # break if 5 syllables
        if syllable == 5:
            return first_line

        tries += 1


def sec_line_generator(adj_dict, noun_dict, verb_dict):
    # second line
    syllable = 0
    tries = 0
    second = False
    possible_seconds = {}

    while second == False:
        if tries == len(adj_dict) or tries == len(noun_dict) or tries == len(verb_dict):
            # sort by value
            sorted_by_value = sorted(
                possible_seconds.items(), key=lambda kv: kv[1], reverse=True)
            for key in sorted_by_value:
                if (key[1]) > 7:
                    continue
                else:
                    second_line = key
                    return second_line[0]

        adj,  adj_syllables = random.choice(list(adj_dict.items()))
        noun, noun_syllables = random.choice(list(noun_dict.items()))
        verb, verb_syllables = random.choice(list(verb_dict.items()))

        # create a dictionary of the adj+noun+verb : total_syllables
        syllable = noun_syllables + adj_syllables + verb_syllables
        second_line = '{} {} {}'.format(adj, noun, verb)
        possible_seconds[second_line] = syllable

        # break if 5 syllables
        if syllable == 7:
            return second_line

        tries += 1


def third_line_generator(adj_dict, noun_dict, verb_dict):
    # third line
    syllable = 0
    tries = 0
    third = False
    possible_thirds = {}

    while third == False:
        if tries == len(adj_dict) or tries == len(noun_dict) or tries == len(verb_dict):
            # sort by value
            sorted_by_value = sorted(
                possible_thirds.items(), key=lambda kv: kv[1], reverse=True)
            for key in sorted_by_value:
                if (key[1]) > 5:
                    continue
                else:
                    third_line = key
                    return third_line[0]

        adj,  adj_syllables = random.choice(list(adj_dict.items()))
        noun, noun_syllables = random.choice(list(noun_dict.items()))
        verb, verb_syllables = random.choice(list(verb_dict.items()))

        # create a dictionary of the adj+noun+verb : total_syllables
        syllable = noun_syllables + adj_syllables + verb_syllables
        third_line = '{} {} {}'.format(adj, noun, verb)
        possible_thirds[third_line] = syllable

        # break if 5 syllables
        if syllable == 5:
            return third_line

        tries += 1


def calculate_sentiment_of_phrase(phrase_list):

    client = language.LanguageServiceClient()
    phrase_sentiment_list = []

    for i in range(len(phrase_list)):

        type_ = enums.Document.Type.PLAIN_TEXT
        document = {'type': type_, 'content': phrase_list[i]}

        resp = client.analyze_sentiment(document)
        sentiment = resp.document_sentiment
        phrase_sentiment_list.append(sentiment.score)
    return phrase_sentiment_list


def main_shit(word_list, final_senti):

    dicti = dictionary.get_syn(word_list)

    noun = find_nouns(dicti)
    verb = find_verbs(dicti)
    adj = find_adjectives(dicti)

    adj_dict = adj_lst_to_dict(adj_to_adj_lst(adj))
    noun_dict = noun_lst_to_dict(noun_to_noun_lst(noun))
    verb_dict = verb_lst_to_dict(verb_to_verb_lst(verb))

    first_line_list = []
    second_line_list = []
    third_line_list = []
    for i in range(5):
        first_line_list.append(first_line_generator(
            adj_dict, noun_dict, verb_dict))
        second_line_list.append(sec_line_generator(
            adj_dict, noun_dict, verb_dict))
        third_line_list.append(third_line_generator(
            adj_dict, noun_dict, verb_dict))

    first_line_senti = calculate_sentiment_of_phrase(first_line_list)
    second_line_senti = calculate_sentiment_of_phrase(second_line_list)
    third_line_senti = calculate_sentiment_of_phrase(third_line_list)

    small = 0
    small = final_senti - first_line_senti[0]
    i = 1
    for i in range(5):
        if(final_senti - first_line_senti[i] <= small):
            small = final_senti - first_line_senti[i]
    i = 0
    for i in range(5):
        if(small == final_senti - first_line_senti[i]):
            break
    small = 0
    small = final_senti - second_line_senti[0]
    j = 1
    for j in range(5):
        if(final_senti - second_line_senti[j] <= small):
            small = final_senti - second_line_senti[i]
    j = 0
    for j in range(5):
        if(small == final_senti - second_line_senti[j]):
            break
    small = 0
    small = final_senti - first_line_senti[0]
    k = 1
    for k in range(5):
        if(final_senti - third_line_senti[k] <= small):
            small = final_senti - third_line_senti[i]
    k = 0
    for k in range(5):
        if(small == final_senti - third_line_senti[k]):
            break

    first_line = first_line_list[i]  # change
    second_line = second_line_list[j]
    third_line = third_line_list[k]

    return first_line, second_line, third_line
