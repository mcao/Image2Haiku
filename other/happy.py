#phrase generator
import random

#https://stackoverflow.com/questions/46759492/syllable-count-in-python
adj = ['happy', 'sad', 'jubilant']
noun = ['dog', 'cat', 'sophia']
verb = ['running', 'sleeping', 'superrcalifragil']

def syllable_count(some_list):
    syllable_list = []

    for i in range(len(some_list)):
        some_list[i] = some_list[i].lower()

        word   = some_list[i]
        count  = 0
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

'''adj_lst = [ ['happy', 'sad', 'jubilant'], [2,1,3]]
noun_lst = [ ['dog', 'cat', 'sophia'], [1,2,3]]
verb_lst = [ ['running', 'sleeping', 'superrcalifragil'], [2,1,7]]'''

def adj_lst_to_dict(adj_lst):
    adj_dict = {}
    for i in range(len(adj_lst)+1):
        adj_dict[ adj_lst[0][i] ] = adj_lst[1][i]

    return adj_dict

def noun_lst_to_dict(noun_lst): #, noun_lst, verb_lst):
    noun_dict = {}
    for i in range(len(noun_lst)+1):
        noun_dict[ noun_lst[0][i] ] = noun_lst[1][i]

    return noun_dict

def verb_lst_to_dict(verb_lst): #, noun_lst, verb_lst):
    verb_dict = {}
    for i in range(len(verb_lst)+1):
        verb_dict[ verb_lst[0][i] ] = verb_lst[1][i]

    return verb_dict

def first_line_generator(adj_dict, noun_dict, verb_dict):
    #first line
    syllable   = 0
    tries      = 0
    first      = False
    possible_firsts = {}

    while first == False:
        if tries == len(adj_dict) or tries == len(noun_dict) or tries == len(verb_dict):
            #sort by value
            sorted_by_value = sorted(possible_firsts.items(), key=lambda kv: kv[1], reverse = True)
            for key in sorted_by_value:
                if (key[1]) > 5:
                    continue
                else:
                    first_line = key
                    return first_line[0]

        adj,  adj_syllables  = random.choice(list(adj_dict.items()))
        noun, noun_syllables = random.choice(list(noun_dict.items()))
        verb, verb_syllables = random.choice(list(verb_dict.items()))
        
        #create a dictionary of the adj+noun+verb : total_syllables
        syllable = noun_syllables + adj_syllables + verb_syllables
        first_line = '{} {} {}'.format(adj, noun, verb)
        possible_firsts[first_line] = syllable

        
        #break if 5 syllables
        if syllable == 5:
            return first_line

        tries += 1

def sec_line_generator(adj_dict, noun_dict, verb_dict):
    #second line
    syllable   = 0
    tries      = 0
    second      = False
    possible_seconds = {}

    while second == False:
        if tries == len(adj_dict) or tries == len(noun_dict) or tries == len(verb_dict):
            #sort by value
            sorted_by_value = sorted(possible_seconds.items(), key=lambda kv: kv[1], reverse = True)
            for key in sorted_by_value:
                if (key[1]) > 7:
                    continue
                else:
                    second_line = key
                    return second_line[0]

        adj,  adj_syllables  = random.choice(list(adj_dict.items()))
        noun, noun_syllables = random.choice(list(noun_dict.items()))
        verb, verb_syllables = random.choice(list(verb_dict.items()))
        
        #create a dictionary of the adj+noun+verb : total_syllables
        syllable = noun_syllables + adj_syllables + verb_syllables
        second_line = '{} {} {}'.format(adj, noun, verb)
        possible_seconds[second_line] = syllable

        
        #break if 5 syllables
        if syllable == 7:
            return second_line

        tries += 1
def third_line_generator(adj_dict, noun_dict, verb_dict):
    #third line
    syllable   = 0
    tries      = 0
    third      = False
    possible_thirds = {}

    while third == False:
        if tries == len(adj_dict) or tries == len(noun_dict) or tries == len(verb_dict):
            #sort by value
            sorted_by_value = sorted(possible_thirds.items(), key=lambda kv: kv[1], reverse = True)
            for key in sorted_by_value:
                if (key[1]) > 5:
                    continue
                else:
                    third_line = key
                    return third_line[0]

        adj,  adj_syllables  = random.choice(list(adj_dict.items()))
        noun, noun_syllables = random.choice(list(noun_dict.items()))
        verb, verb_syllables = random.choice(list(verb_dict.items()))
        
        #create a dictionary of the adj+noun+verb : total_syllables
        syllable = noun_syllables + adj_syllables + verb_syllables
        third_line = '{} {} {}'.format(adj, noun, verb)
        possible_thirds[third_line] = syllable

        
        #break if 5 syllables
        if syllable == 5:
            return third_line

        tries += 1

if __name__ == "__main__":
    adj_lst = adj_to_adj_lst(adj)
    noun_lst = noun_to_noun_lst(noun)
    verb_lst = verb_to_verb_lst(verb)
    adj_dict = adj_lst_to_dict(adj_lst)
    noun_dict = noun_lst_to_dict(noun_lst)
    verb_dict = verb_lst_to_dict(verb_lst)
    print(first_line_generator(adj_dict, noun_dict, verb_dict))
    print(sec_line_generator(adj_dict, noun_dict, verb_dict))
    print(third_line_generator(adj_dict, noun_dict, verb_dict))