#Linear search is a sequential searching algorithm where it starts form one end and check every element of the list until the target element is found.

array = [2,3,1,5,9,7,6,10]
n = len(array)
def linearsearch(array, target):
    for i in range(n):
        if array[i] == target:
            return i
    return -1
target = 7
result = linearsearch(array, target)

if result != 0:
    print("Value", target, "found")