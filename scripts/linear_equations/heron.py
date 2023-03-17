#### Formula:
#### S=sqrt(p(p-a)(p-b)(p-c))
#### S --> triangle area
#### p = (a+b+c)/2
from math import sqrt


def herons_formula(a, b, c):
    p = (a+b+c)/2
    temp = p*(p-a)*(p-b)*(p-c)

    if temp <= 0:
        return(print("Wara!"))

    S = sqrt(temp)
    
    return S

