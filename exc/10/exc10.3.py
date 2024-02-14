def anagramCheck(txt1, txt2):
    if len(txt1) != len(txt2):
        return False
    tab1 = []
    tab2 = []

    for i in range(len(txt1)):
        tab1.append(txt1[i])
        tab2.append(txt2[i])

    for j in range(len(tab1)-1):
        for i in range(len(tab1)-1):
            if tab1[i] > tab1[i + 1]:
                tmp = tab1[i]
                tab1[i] = tab1[i + 1]
                tab1[i + 1] = tmp

        for i in range(len(tab2)-1):
            if tab2[i] > tab2[i + 1]:
                tmp = tab2[i]
                tab2[i] = tab2[i + 1]
                tab2[i + 1] = tmp

    return tab1 == tab2

txt1 = "alergia"
txt2 = "galeria"
print(anagramCheck(txt1, txt2))
txt1 = "ekran"
txt2 = "nerka"
print(anagramCheck(txt1, txt2))