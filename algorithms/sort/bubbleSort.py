dane = [9, 8, 7, 5, 5]

def bubbleSort(data):
    # Bubble sort operates n-1 times
    for i in range(len(data)-1):
        # Check every value in table
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                #Changing values
                storage = data[i]
                data[i] = data[i+1]
                data[i+1] = storage
    return data

print(bubbleSort(dane))