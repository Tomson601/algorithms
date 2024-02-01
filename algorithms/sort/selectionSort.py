dane = [9, 8, 7, 5, 5, 7, 3]

def selectionSort(data):
    for j in range(len(data)-1):
        lowest_number_index = j

        for i in range(j+1, len(data)):
            if data[i] < data[lowest_number_index]:
                lowest_number_index = i
            # Changing values
            storage = data[j]
            data[j] = data[lowest_number_index]
            data[lowest_number_index] = storage
    return data

print(selectionSort(dane))