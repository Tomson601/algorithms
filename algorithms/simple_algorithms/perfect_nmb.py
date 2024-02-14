def is_perfect(nmb):
    dividers = []

    for i in range(1, nmb):
        if nmb % i == 0:
            dividers.append(i)

    div_sum = 0
    for i in dividers:
        div_sum += i

    return div_sum == nmb

print(is_perfect(6))
