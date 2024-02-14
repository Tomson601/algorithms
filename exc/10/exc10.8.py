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
    range_of_elements = max_value - min_value + 1

    buckets = [0] * range_of_elements
    sorted_arr = []

    for i in range(len(data)):
        buckets[data[i] - min_value] += 1

    for i in range(range_of_elements):
        if buckets[i] != 0:
            for j in range(buckets[i]):
                sorted_arr.append(i + min_value)

    return sorted_arr


print(bucketSort([5, -8, 7, -2, 3, 2, 6, 8]))
