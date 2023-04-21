def minimumSwaps(arr):
    print(arr)
    temp = []
    for i in range(len(arr)):
        temp.append((arr[i],i))
    print(temp)
    temp.sort()
    for i in range (len(temp)):
        idx = temp[i][1]
        if idx != i:
            temp[i],temp[idx]=temp[idx],temp[i]
            i -= 1
    print(temp)


print(minimumSwaps([1,3,5,2,4,6,7]))