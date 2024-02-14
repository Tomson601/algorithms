# Napisz program, który obliczy iteracyjnie NWD z wpisanych przez użytkownika liczb.

def NWD_iterate(nmb1, nmb2):
    div_nmb1 = []
    div_nmb2 = []

    for i in range(1, nmb1+1):
        if nmb1 % i == 0:
            div_nmb1.append(i)

    for i in range(1, nmb2+1):
        if nmb2 % i == 0:
            div_nmb2.append(i)

    for i in div_nmb1:
        if i in div_nmb2:
            nwd = i

    return nwd

print(NWD_iterate(10, 2))
