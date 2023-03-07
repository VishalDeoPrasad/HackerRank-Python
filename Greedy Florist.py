def getMinimumCost(k, c):
    if len(c) == k:
        return sum(c)
    c.sort(reverse=True)
    summ = 0
    m = 1
    for i in range(len(c)):
        summ += c[i] * m
        if (i+1) % k == 0:
            m += 1
    return summ

print(getMinimumCost(3, [1,3,5,7,9]))