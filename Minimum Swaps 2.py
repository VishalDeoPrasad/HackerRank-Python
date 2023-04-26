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

def minimumSwaps(arr):
    arr_set = [(arr[i], i) for i in range(len(arr))]
    print(arr_set)
    arr_set.sort()
    print(arr_set)
    for i in range(len(arr_set)):
        idx = arr_set[i][1]
        while i != idx:
            arr_set[idx], arr_set[i] = arr_set[i], arr_set[idx]
            

    return arr_set
print(minimumSwaps([7,1,3,2,4,5,6]))