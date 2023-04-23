def balancedSums(arr):
    left,right = 0,sum(arr)
    for i in range(len(arr)):
        right -= arr[i]
        if left == right:
            return "YES"
        left += arr[i]
    return "NO"

print(balancedSums([1,6,6,3,4]))