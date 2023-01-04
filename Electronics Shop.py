def getMoneySpent1(keyboards, drives, b):
    max_price = 0 #
    for k in keyboards:
        for d in drives:
            if (k+d) > max_price and (k+d) <= b:
                max_price = k+d
    if max_price != 0:
        return max_price
    else:
        return -1

def getMoneySpent2(keyboards, drives, b):
    max_price = 0 #
    [max_price := k+d for k in keyboards for d in drives if (k+d) > max_price and (k+d) <= b]
    return max_price if max_price != 0 else -1         

def getMoneySpent(keyboards, drives, s):
    return max(x+y for x in keyboards for y in drives if (x+y) <= s)

print(getMoneySpent([3,1],[5,2,8], 10))
