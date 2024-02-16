def wyznaczPivot(tablica, l_index, r_index):
    pivot_value = tablica[r_index]
    smaller_index = l_index - 1

    for i in range(l_index, r_index):
        if tablica[i] < pivot_value:
            smaller_index += 1
            tablica[i], tablica[smaller_index] = tablica[smaller_index], tablica[i]

    tablica[smaller_index + 1], tablica[r_index] = tablica[r_index], tablica[smaller_index + 1]

    return smaller_index + 1


def quickSort(tablica, l_index, r_index):
    if l_index < r_index:
        pivot = wyznaczPivot(tablica, l_index, r_index)
        quickSort(tablica, l_index, pivot - 1)
        quickSort(tablica, pivot + 1, r_index)


napis = "konstantynopolitańczykowianeczka"
napis_tablica = list(napis)
dlugosc_napisu = len(napis)
quickSort(napis_tablica, 0, dlugosc_napisu - 1)
napis_posortowany = ''.join(napis_tablica)
print(napis_posortowany)
