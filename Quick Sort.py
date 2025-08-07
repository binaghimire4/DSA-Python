#quicksort is a comparasion-based sorting algorithm that utilizes a divide and conquer strategy. It works by partitioning an array into two sub-array around a chosen "pivot" element.

def quick_sort(list):
    if len(list) < 1:
        return list
    else:
        pivot = list.pop()

    lower_list = []
    higher_list = []

    for i in list:
        if i < pivot:
           lower_list.append(i)
        else:
            higher_list.append(i)
    return quick_sort(lower_list) + [pivot] + quick_sort(higher_list)

print(quick_sort([23,45,15,11,67,89,78]))

