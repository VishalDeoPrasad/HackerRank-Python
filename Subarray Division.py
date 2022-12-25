def birthday(s, d, m):
    n = len(s)
    ways = 0
    [ways := ways + 1 for i in range(n-m+1) if sum(s[i:i+m]) == d]
    return ways

print(birthday([2,2,1,3,2], 4, 2))