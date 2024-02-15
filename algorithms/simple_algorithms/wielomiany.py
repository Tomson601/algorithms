def wielomian(wspolczynniki, x, stopien):
    if stopien == 0:
        return wspolczynniki[stopien]
    else:
        return x * wielomian(wspolczynniki, x, stopien-1) + wspolczynniki[stopien]


print(wielomian([2, 1, 3, 9], 10, 3))

def wielomian_iter(wspolczynniki, x, stopien):
    wartosc = 0

    for i in range(stopien, -1, -1):
        wartosc += wspolczynniki[stopien-i] * (x ** i)
    return wartosc

print(wielomian_iter([2, 1, 3, 9], 10, 3))
