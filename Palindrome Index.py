def palindromeIndex(s):
    s = list(s[:])
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            new_s = s[:i]+s[i+1:]
            if new_s == new_s[::-1]:
                return i
            else:
                return n-i-1
    return -1
s = 'baaa'
print(palindromeIndex(s))