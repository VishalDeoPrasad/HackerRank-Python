def lonelyinteger(a):
    n = a[0]
    for i in range(1, len(a)):
        n = n^a[i]
    return n

print(lonelyinteger([1,2,3,4,3,2,1]))