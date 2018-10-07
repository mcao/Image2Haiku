#https://stackoverflow.com/questions/46759492/syllable-count-in-python

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
#noun_sylla_list = syllable_count(noun_list)
#main_noun_list = [noun_list,noun_sylla_list]
