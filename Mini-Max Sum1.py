def miniMaxSum(arr):
    minn = min(arr)
    maxx = max(arr)
    print( sum(arr)-maxx, sum(arr)-minn)

arr = [1,5, 10, 3,5,7,9]
miniMaxSum(arr)