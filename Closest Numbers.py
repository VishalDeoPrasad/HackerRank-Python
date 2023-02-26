def closestNumbers(arr):
    arr.sort()
    min_diff = abs(arr[1]-arr[0])
    pair_list = []
    for i in range(len(arr)-1):
        curr_diff = abs(arr[i+1]-arr[i])
        if curr_diff < min_diff:
            pair_list = []
            min_diff = curr_diff
        if curr_diff == min_diff:
            pair_list.append(arr[i])
            pair_list.append(arr[i+1])
    return pair_list

print(closestNumbers([5,2,3,4,1]))