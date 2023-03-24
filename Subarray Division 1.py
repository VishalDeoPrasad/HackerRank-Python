def ArraySum(s, i, j):
    summ = 0
    for l in range(i, j):
        summ += s[l]
    return summ
        
def birthday1(s, d, m):
    cnt = 0
    for i in range(len(s)-m+1):
        j = i+m
        summ = ArraySum(s, i, j)
        if summ == d:
            cnt += 1
    return cnt

def birthday(s, d, m):
    temp = sum(s[:m])
    cnt = 0
    if temp == d:
        cnt += 1
    for i in range(m, len(s)):
        temp = temp+s[i]-s[i-m]
        if temp == d:
            cnt += 1
    return cnt
        
        
print(birthday([2,2,1,3,2], 4, 2))