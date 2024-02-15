# Napisz program, który obliczy rekurencyjnie Silnie z wpisanej przez użytkownika liczby.
def silnia(liczba):
    if liczba == 1 or liczba == 0:
        return 1
    else:
        return silnia(liczba-1) * liczba

print(silnia(4))
