def wielomian(wspolczynniki, x, stopien):
    if stopien == 0:
        return wspolczynniki[stopien]
    else:
        return x * wielomian(wspolczynniki, x, stopien-1) + wspolczynniki[stopien]


print(wielomian([2, 1, 3, 9], 10, 3))
