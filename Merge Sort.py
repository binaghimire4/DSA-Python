#Merge sort is a divide and conquer algorithm. It divides input array in tow halves, calls itself for the tow halves and then merges the sorted half.

def mergesort(array):
    if len(array) <= 1:
        return array

    mid = len(array)//2

    leftHalf = array[:mid]
    rightHalf = array[mid:]

    sortedleft = mergesort(leftHalf)
    sortedright = mergesort(rightHalf)

    return merge(sortedleft, sortedright)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

list = [2,5,71,8,0,19, 10]
sortedlist = mergesort(list)
print("Merge Sort:", sortedlist)



