dane = [9, 8, 5, 5, 7, 3]

def selectionSort(data):
    for i in range(len(data)-1):
        lowest_number_index = i

        for j in range(i+1, len(data)):
            if data[j] < data[lowest_number_index]:
                lowest_number_index = j
            # Changing values
            storage = data[i]
            data[i] = data[lowest_number_index]
            data[lowest_number_index] = storage
    return data

print(selectionSort(dane))