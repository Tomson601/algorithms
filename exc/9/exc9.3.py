def NWD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def NWW(a, b):
    return int((a * b)/NWD(a, b))

print(NWW(2, 6))
