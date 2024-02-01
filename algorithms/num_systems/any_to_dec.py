# Napisz program, który zamienia liczby z systemu dowolnego na decymalny. (Spróbuj nie przepisywać kodu z lekcji.)

def anyToDec(number, system):
    wynik = 0
    litery = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

    for i in range(0, len(number)):
        power = len(number) - 1 - i
        if number[i] in litery:
            wynik = wynik + (litery[number[i]]*system**power)
        else:
            wynik = wynik + int(number[i])*system**power
    return wynik

wynik = anyToDec("1221021", 3)
print(wynik)
