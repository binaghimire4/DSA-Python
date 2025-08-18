#counting sort is a non-comparision based an algorthm that sorts an array by counting how many times each element appears and using those counts to build a new sorted array.

def countsort(array):
    max_val = max(array)
    count = [0]* (max_val + 1)

    while len(array) > 0:
        num = array.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i]-= 1
    return array

array = [11,9,4,1,2,44,56,76, 89]
sorted = countsort(array)
print("Sorted array:", sorted)

def count(array):
    if not array:
        return []
    max_val = max(array)
    count = [0]*(max_val + 1)

    for i in array:
        count[i]+= 1
    sorted_array = []
    for item in range(len(count)):
        sorted_array.extend([item]*count[item])

    return sorted_array
array = [26,67,34,12,11,0]
sorted = count(array)
print(sorted)

