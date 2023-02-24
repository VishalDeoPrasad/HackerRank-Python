#solved on o(n*n)
def minimumAbsoluteDifference1(arr):
    min_sum = abs(arr[0]-arr[1])
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            temp_sum = abs(arr[i]-arr[j])
            if temp_sum < min_sum:
                min_sum = temp_sum
    return min_sum

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = abs(arr[0]-arr[1])
    for i in range(1,len(arr)-1):
        temp_diff = abs(arr[i]-arr[i+1])
        if temp_diff < min_diff:
            min_diff = temp_diff
    return min_diff
            
print(minimumAbsoluteDifference([-2,2,4]))