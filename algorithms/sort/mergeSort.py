#TODO



# def merge(tablica, lewy_index, pivot, prawy_index, tmp_table):
#     for i in range(lewy_index, prawy_index+1):
#         tmp_table[i] = tablica[i]
#
#     indexLewy = lewy_index
#     indexPrawy = pivot+1
#     print("MERGE")
#     print(lewy_index, pivot, prawy_index)
#
# def mergeSort(tablica, lewy_index, prawy_index, tmp_table):
#     if lewy_index != prawy_index:
#         pivot = int((lewy_index+prawy_index)/2)
#         mergeSort(tablica, lewy_index, pivot, tmp_table)
#         mergeSort(tablica, pivot+1, prawy_index, tmp_table)
#         merge(tablica, lewy_index, pivot, prawy_index, tmp_table)
#
#
# tablica = [5, 8, 7, 2, 3, 2, 6, 8]
# tmp_table = [0, 0, 0, 0, 0, 0, 0, 0]
# left_index = 0
# right_index = 7
#
# print(mergeSort(tablica, left_index, right_index))
