def char_count(char, word):
    counter = 0
    for i in word:
        if i == char:
            counter += 1
    return counter

def is_anagram(key, word):
    if len(key) != len(word):
        return False
    else:
        for i in range(len(key)):
            char = key[i].lower()
            if char_count(char, key.lower()) != char_count(char, word.lower()):
                return False
    return True


print(is_anagram("mama", "amma"))
