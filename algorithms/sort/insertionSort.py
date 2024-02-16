tablica = [8,1,2,3,7,8,2,1,4]

def insertionSort(tablica):
    for granica in range(1, len(tablica)):
        index = granica - 1
        wartoscElementu = tablica[granica]

        while index >= 0 and tablica[index] > wartoscElementu:
            tablica[index + 1] = tablica[index]
            index -= 1
        tablica[index + 1] = wartoscElementu
    return tablica

print(insertionSort(tablica))
