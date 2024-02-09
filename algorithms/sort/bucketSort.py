def findMax(tablica):
    value = tablica[0]
    for i in range(len(tablica)):
        if tablica[i] > value:
            value = tablica[i]

    return value

def bucketSort(tablica):
    max_value = findMax(tablica)
    buckets = []
    sorted_arr = []

    for i in range(max_value + 1):
        buckets.append(0)

    for i in range(len(tablica)):
        numer = tablica[i] - 1
        buckets[numer] += 1

    for i in range(max_value + 1):
        for j in range(buckets[i]):
            sorted_arr.append(i+1)

    return sorted_arr

tablica = [5, 8, 7, 2, 3, 2, 6, 8]
print(bucketSort(tablica))
