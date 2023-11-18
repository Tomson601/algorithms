a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))

def NWD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

wynik = NWD(a, b)
print(wynik)
