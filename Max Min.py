def maxMin(k, arr):
    arr.sort()
    min_diff = 9999999999
    n = len(arr)
    for i in range(n-k+1):
        j = i+k-1
        if (arr[j]-arr[i]) < min_diff:
            min_diff = arr[j]-arr[i]
    return min_diff

print(maxMin(4, [1,2,3,4,10,20,30,40,100,200]))