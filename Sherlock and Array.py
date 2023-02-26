def prefixArray(arr):
    pf = []
    pf.append(arr[0])
    for i in range(1,len(arr)):
        pf.append(pf[i-1]+arr[i])
    return pf
        

def balancedSums(arr):
    pf = prefixArray(arr)
    n = len(arr)
    for i in range(n):
        if i == 0:
            left = 0 
            right = pf[n-1] - pf[i]
            if left == right:
                return "YES"
        else:
            left = pf[i-1]
            right = pf[n-1] - pf[i]
            if left == right:
                return "YES"
    return "NO"

print(balancedSums([5,6,8,11]))
                