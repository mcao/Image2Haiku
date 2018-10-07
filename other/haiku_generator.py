#phrase generator
import random

adj_lst = [ ['happy', 'sad', 'jubilant'], [2,1,3]]
noun_lst = [ ['dog', 'cat', 'sophia'], [1,2,3]]
verb_lst = [ ['running', 'sleeping', 'superrcalifragil'], [2,1,7]]

#noun_dict = {"dog":1, "cat":2, "sophia":3}
#adj_dict  = {"happy":2, "sad":1, "jubilant":3}
#verb_dict = {"running":2, "sleeping":1, "supercalifragil":7}

def adj_lst_to_dict(adj_lst): #, noun_lst, verb_lst):
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
    adj_dict = adj_lst_to_dict(adj_lst)
    noun_dict = noun_lst_to_dict(noun_lst)
    verb_dict = verb_lst_to_dict(verb_lst)
    print(first_line_generator(adj_dict, noun_dict, verb_dict))
    print(sec_line_generator(adj_dict, noun_dict, verb_dict))
    print(third_line_generator(adj_dict, noun_dict, verb_dict))