def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # Inicjalizacja lewej i prawej połowy jako puste listy
        left_half = []
        right_half = []

        # Podział listy na lewą i prawą połowę
        for i in range(mid):
            left_half.append(arr[i])
        for i in range(mid, len(arr)):
            right_half.append(arr[i])

        # Rekurencyjne sortowanie obu połówek
        merge_sort(left_half)
        merge_sort(right_half)

        # Scalanie posortowanych połówek
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Dodanie pozostałych elementów z lewej połowy (jeśli istnieją)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Dodanie pozostałych elementów z prawej połowy (jeśli istnieją)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        return arr

# Przykładowe użycie
arr = [2, 9, 8, 5, 3, 2, 1, 9, 6]
print(merge_sort(arr))
