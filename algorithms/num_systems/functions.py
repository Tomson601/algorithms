# liczba = int(input("Podaj liczbe do przeliczenia: "))
# system = int(input("Podaj na jaki system przeliczyc liczbe: "))
# litery = {
#     "10": "A",
#     "11": "B",
#     "12": "C",
#     "13": "D",
#     "14": "E",
#     "15": "F",
# }

def decToAny(liczba, system):
    wynik = ""
    while liczba > 0:
        reszta = liczba % system
        liczba = liczba // system
        if reszta >= 10:
            # Dictionary:
            #wynik = litery[str(reszta)] + wynik
            # ASCII:
            wynik = chr(55 + reszta) + wynik
        else:
            wynik = str(reszta) + wynik
    return wynik

def charToDigit(character):
    if ord(character) >= 65:
        return ord(character) - 55
    return int(character)

def anyToDec(napis, system):
    dec = 0
    for i in range(0, len(napis)):
        power = len(napis)-1-i
        dec = dec + charToDigit(napis[i]) * (system ** power)
    return dec

wynik = anyToDec("10F", 16)
print(wynik)