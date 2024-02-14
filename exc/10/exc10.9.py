input_file_path = "../../data/Dane_PR/anagram.txt"
output_file_path = "../../data/odp/odp_4a.txt"
output_file_path2 = "../../data/odp/odp_4b.txt"

def selectionSort(data):
    data_table = []
    for txt in data:
        data_table.append(txt)

    for j in range(len(data_table)-1):
        lowest_number_index = j

        for i in range(j+1, len(data_table)):
            if data_table[i] < data_table[lowest_number_index]:
                lowest_number_index = i
            # Changing values
        data_table[j], data_table[lowest_number_index] = data_table[lowest_number_index], data_table[j]
    return data_table


def anagramCheck(key, txt_table):
    sorted_key = selectionSort(key)

    for txt in txt_table:
        sorted_txt = selectionSort(txt)
        if sorted_key != sorted_txt:
            return False
    return True


with open(input_file_path) as infile:
    data = infile.readlines()

outfile = open(output_file_path, "w")
outfile2 = open(output_file_path2, "w")

for line in data:
    text = line.replace("\n", "")
    text_table = text.split()

    length = len(text_table[0])
    flag = True

    for i in range(len(text_table)):
        if len(text_table[i]) != length:
            flag = False
    if flag:
        ready_txt = ""
        anagram_txt = ""

        if anagramCheck(text_table[0], text_table):
            for txt in text_table:
                anagram_txt += txt + " "
            outfile2.write(anagram_txt)
            outfile2.write("\n")

        for txt in text_table:
            ready_txt += txt + " "
        outfile.write(ready_txt)
        outfile.write("\n")


outfile.close()
outfile2.close()
