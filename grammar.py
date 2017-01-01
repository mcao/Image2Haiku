#File: Grammar
#By Michael DeLeo
#Grammar is a set of helper functions to assist the primary function sentence_former
#there is already a file for the generation of a sentence, but this will help
#to make the sentence make more sense, or even help to form a better sentence

#TODO: Should figure out a way to include prepositions so it makes more sense

#grammar
#note, it does not work with one word or more than three atm
def grammer_fix(sentence):
    #take the sentence, if an adjective is after a noun then switch

    #sentence structure cases for now:
    #[adjective] [noun]
    #[adjective] [adjective] [noun]
    #[noun] [verb] [adverb]
    #[verb] [noun]
    #[noun] [verb]
    words = sentence.split(" ")
    sz = len(words) #number of words

    for x in range(0,sz):
        #make an object of the word with type
        words_list.append({x:{words[x]:check_word_type(words[x])}})
    #now i have the list of objects

    qualifiers = {0:{2:"adjective noun"},
                 1:{3:"adjective adjective noun"},
                 2:{3:"noun verb adverb"},
                 3:{2:"verb noun"},
                 4:{2:"noun verb"},
                 5:{3:"preposition adjective noun"}}
    #{index of case : # of words : word type order}

    q_sz = len(qualifiers)

    type_list = make_type_list(words_list,words)
    for x in range(0,q_sz): #loop to go through qualifiers
        for y in range(0,sz):   #loop to go through word list
            try:
                qualifiers_score.append(word_type_matches(qualifiers[x][sz],type_list))
            except:
                #tries to use size of 3 for 3 words instead of 2
                qualifiers_score.append(word_type_matches(qualifiers[x][sz+1],type_list))
    #now assume i have the closest matches
    #find the best one, and match the word order to it

    #TODO: find best one
    mx = 0
    index = 0
    for x in range(0,len(qualifiers_score)):
        if (qualifiers_score[x] > mx):
            mx = qualifiers_score[x]
            index = x
    for x in range(0,5):
        try:
            best = qualifiers[index][x] #it will be in this variable, dont know the size

    new_sentence = replace_type_with_word(best,words_list,words)
    
    return new_sentence


#forms the sentence from the wordlist
#TODO: how it decides which words
def sentence_former(words, req_syl):
    sentence = ""
    #TODO
    return sentence

#switches the words at pos1 and pos2 of a word list
def switch_words(pos1,pos2,sentence):
    new_sentence = sentence
    temp = new_sentence[pos1]
    new_sentence[pos1] = new_sentence[pos2]
    new_sentence[pos2] = temp

    return new_sentence


#return strings of "adjective", "noun", "verb", "adverb"
def check_word_type(word):
    #first check the chache file about the word
    #if no cache then go to oxford and add to the cache
    #TODO

    return "adj"

#returns a full string from a string list
def pull_it_together(sentence):
    sz = len(sentence)
    for x in range(0,sz):
        str += " " + sentence[x]

    return str

#creates a type list of the words
def make_type_list(words_list,words):
    for x in range(0, len(words_list)):
        str.append(words_list[x][words[x]])
    return str

#returns the number of matches from the type list. does not double dip,
#a match is deleted from the list
#CONDITIONS: requires type_list to be string, and word_types to be string list
def word_type_matches(type_list,word_types):
    

def replace_type_with_word(type_str,words_list,words):
    type_list = type_str.split(" ")
    #put the word into its spot that matches the type
    for x in (0, len(words_list)):
        if (type_list[x] == words_list[x][words[x]]):
            type_list[x] = words[x]

    return pull_it_together(type_list)
