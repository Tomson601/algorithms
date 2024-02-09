def max_val(arr):
    value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > value:
            value = arr[i]

    return value

def min_val(arr):
    value = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < value:
            value = arr[i]

    return value

def bucketSort(data):
    max_value = max_val(data)
    min_value = min_val(data)
    buckets = []
    sorted_arr = []

    for i in range(max_value+1):
        buckets.append(0)

    for i in range(len(data)-1, -1, -1):
        buckets[data[i]-1] += 1

    for i in range(len(data)-1, -1, -1):
        if buckets[i] != 0:
            for j in range(buckets[i]):
                sorted_arr.append(i+1)

    return sorted_arr

print(bucketSort([5, 8, 7, 2, 3, 2, 6, 8]))
