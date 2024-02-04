def selectionSortAscending(data_in):
    for j in range(len(data_in)):
        lowest_number_index = j

        for i in range(j+1, len(data_in)):
            if data_in[i] < data_in[lowest_number_index]:
                lowest_number_index = i

        if lowest_number_index != j:
            tmp = data_in[j]
            data_in[j] = data_in[lowest_number_index]
            data_in[lowest_number_index] = tmp

    return data_in


print(selectionSortAscending([7, 2, 5, 2, 6, 9, 9, 1]))