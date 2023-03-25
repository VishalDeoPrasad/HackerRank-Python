def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n%2 != 0:
        return arr[n//2]
    a = arr[(n//2)-1]
    b = arr[n//2]
    return (a+b)/2

print(findMedian([5,0,0,0,0]))