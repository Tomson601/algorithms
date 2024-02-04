input_file_path = "../data/odp/odp_4a.txt"
output_file_path = "../data/odp/odp_4b.txt"

with open(input_file_path) as infile:
    data = infile.readlines()

outfile = open(output_file_path, "w")

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
        for txt in text_table:
            ready_txt += txt + " "
        outfile.write(ready_txt)
        outfile.write("\n")


outfile.close()
