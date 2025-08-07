#Radix sort algorithm is a sorts an array by individual digits, starting with the least significant digit.

arr = [3,5,7,8,1,9,0,4,2,6]
max_val = max(arr)
exp = 1
radixArray = [[],[],[],[],[],[],[],[],[],[]]

while max_val // exp > 0:

        while len(arr) > 0:
            val = arr.pop()
            radixIndex = (val //exp)%10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)
        exp*= 10

print("Sorted array:", arr)

