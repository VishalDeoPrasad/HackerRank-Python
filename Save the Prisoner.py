def saveThePrisoner2(n, m, s):
    if (m+s-1) % n:
        return (m+s-1) % n
    return n

def saveThePrisoner1(n, m, s):
    rotation = m + s - 1
    last = rotation % n
    if last == 0:
        return n
    return last

def saveThePrisoner(n, m, s):
    return (m+s-1)%n if (m+s-1)%n else n

print(saveThePrisoner(7, 19, 2))
