#Binary search is an algorithm which is used to find a specific target element within a sorted array or list. It operates by reparedly dividing the search interval in half.

def binarysearch(array, target):
    left = 0
    right = len(array) -1

    while left <= right:
        mid = (left + right)//2

        if array[mid]==target:
             return mid
        if array[mid] < target:
             left = mid + 1
        else:
             right = mid -1
    return -1

array = [10,23,45,56,76,43,22]
target = 56

result = binarysearch(array, target)
if result != -1:
    print("Value", target, "found at index", result)
else:
    print("Target not found in array")

