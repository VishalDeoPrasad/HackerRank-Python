def diagonalDifference(arr):
    # Write your code here
    left_diagonal = 0
    right_diagonal = 0
    [left_diagonal := left_diagonal + arr[i][i] for i in range(len(arr))]
    [right_diagonal := right_diagonal + arr[i][j] for i in range(len(arr)) for j in range(len(arr)) if i+j==len(arr)-1]
    return abs(left_diagonal - right_diagonal)

arr = [[7,1,5],[1,2,3],[4,0,6]]
print(diagonalDifference(arr))  
