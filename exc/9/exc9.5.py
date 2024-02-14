# Napisz program, który obliczy iteracyjnie Silnie z wpisanej przez użytkownika liczby.
def silnia(liczba):
    iloczyn = 1
    for i in range(1, liczba+1):
        iloczyn = iloczyn * i
    return iloczyn

print(silnia(5))
