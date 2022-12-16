def miniMaxSum(arr):
    arr.sort()
    #print(arr)
    print(sum(arr[:4]), sum(arr[-4:]))
arr = [1,5, 10, 3,5,7,9]
miniMaxSum(arr)