# Napisz program, który zamienia liczby z systemu decymalnego na binarny. (Spróbuj nie przepisywać kodu z lekcji.)

def decToBin(number):
    wynik = ""
    while number > 0:
        reszta = number % 2
        number = number // 2
        wynik = str(reszta) + wynik
    return wynik

wynik = decToBin(128)
print(wynik)
wynik = decToBin(21)
print(wynik)