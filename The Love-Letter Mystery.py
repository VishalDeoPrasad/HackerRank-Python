def theLoveLetterMystery(s):
    cnt = 0
    n = len(s)
    for i in range(n//2):
        cnt += abs(ord(s[i]) - ord(s[n-i-1]))
    return cnt

print(theLoveLetterMystery("cde"))