def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i]+B[i] < k:
            return "NO"
    return "YES"
A = [2, 1, 3]
B = [7, 8, 9]
print(twoArrays(10, A,B))