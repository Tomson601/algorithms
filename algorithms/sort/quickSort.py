tablica = [8,1,2,3,7,8,2,1,4]

# TODO: Beautify and split this
def wyznaczPivot(tablica, l_index, r_index):
    for i in range(l_index, r_index):
        if tablica[i] < tablica[r_index]:
            tmp = tablica[i]
            tablica[i] = tablica[l_index]
            tablica[l_index] = tmp
            l_index += 1

    zmiana_pivot = tablica[l_index]
    tablica[l_index] = tablica[r_index]
    tablica[r_index] = zmiana_pivot

    return l_index


def quickSort(tablica, l_index, r_index):
    if l_index < r_index:
        pivot = wyznaczPivot(tablica, l_index, r_index)
        quickSort(tablica, l_index, pivot - 1)
        quickSort(tablica, pivot + 1, r_index)


quickSort(tablica, 0, 8)
print(tablica)
