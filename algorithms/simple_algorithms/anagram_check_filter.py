def bubbleSort(wyraz):
    tablica = []
    for i in range(len(wyraz)):
        tablica.append(wyraz[i])

    for i in range(len(tablica)-1):
        for j in range(len(tablica)-1):
            if tablica[j] > tablica[j+1]:
                tmp = tablica[j]
                tablica[j] = tablica[j+1]
                tablica[j+1] = tmp

    wyraz_sort = ""
    for i in range(len(tablica)):
        wyraz_sort += tablica[i]

    return wyraz_sort

def is_anagram(wyr1, wyr2):
    if len(wyr1) != len(wyr2):
        return False
    else:
        sorted_wyr1 = bubbleSort(wyr1)
        sorted_wyr2 = bubbleSort(wyr2)
        print(sorted_wyr1, sorted_wyr2)
        if sorted_wyr1 != sorted_wyr2:
            return False
    return True

print(is_anagram("mama", "amma"))
print(is_anagram("alan", "nala"))
