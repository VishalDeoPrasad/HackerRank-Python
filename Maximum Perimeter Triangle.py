def maximumPerimeterTriangle(sticks):
    sticks.sort()
    temp = []
    i = len(sticks)-3
    while i>=0:
        if sticks[i]+sticks[i+1] > sticks[i+2]:
            temp.append([sticks[i], sticks[i+1], sticks[i+2]])
            break
        else:
            i -= 1
    if len(temp) > 0:
        return temp[0]
    return [-1]

print(maximumPerimeterTriangle([1,2,3,4]))