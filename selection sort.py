#Selection sort is a simple sorting algorithm that repeatedly selects the smallest element from an unsorted list and places it at the beginning.

my_array = [56,76,4,532,12,90,55]
n = len(my_array)
for i in range(n -1):
    min_index = i
    for j in range(i+1, n):
        if my_array[j] < my_array[min_index]:
            min_index = j
    my_array[i], my_array[min_index] = my_array[min_index], my_array[i]
print("Sorted array:", my_array)
