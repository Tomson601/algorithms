#Napisz program, który realizuje sortowanie tablicy malejąco za pomocą algorytmu sortowania bąbelkowego.

def bubbleSortDescending(data_in):
    for j in range(len(data_in)-1):
        for i in range(len(data_in)-1):
            if data_in[i] < data_in[i+1]:
                #Shuffle values
                tmp = data_in[i]
                data_in[i] = data_in[i+1]
                data_in[i+1] = tmp
    return data_in


data = [9, 2, 3, 8, 1, 7, 6, 2, 5]
print(bubbleSortDescending(data))