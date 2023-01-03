def getMoneySpent(keyboards, drives, b):
    max_price = 0 #
    for k in keyboards:
        for d in drives:
            if (k+d) > max_price and (k+d) <= b:
                max_price = k+d
    if max_price != 0:
        return max_price
    else:
        return -1

print(getMoneySpent([3,1],[5,2,8], 10))
