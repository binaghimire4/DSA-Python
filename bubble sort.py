#Bubble sort is a simple sorting algorithm that works by repeatedly comparing and swapping adjacent elements in a
# list until they are in the asecending order. They also also known as sinking sort or exchange sort.

my_array = [3,5,1,2,9,7,8]
n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j + 1]:
            my_array[j], my_array[j + 1] = my_array[j+1], my_array[j]

print("sorted array:", my_array)