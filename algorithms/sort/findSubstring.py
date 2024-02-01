def findSubstring(dane, wzor):
    znalezione = 0
    i = 0
    while i < len(dane):
        if dane[i] == wzor[znalezione]:
            znalezione += 1
            if znalezione == len(wzor):
                return True
        else:
            if znalezione > 0:
                i -= 1
            znalezione = 0
        i += 1
    return False


print(findSubstring("LOTNISKO", "LOT"))
print(findSubstring("XXXLOTXX", "LOT"))
print(findSubstring("LOLOLLOTT", "LOT"))
