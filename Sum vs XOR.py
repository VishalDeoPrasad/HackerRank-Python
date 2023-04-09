def sumXor(n):
    ans = 1
    while n:
        b = n&1
        n >>= 1
        if b == 0:
            ans *= 2
    return ans

print(sumXor(10))