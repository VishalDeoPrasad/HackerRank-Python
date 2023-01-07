def hurdleRace(k, height):
    # Write your code here
    return 0 if max(height)<k else max(height) - k

print(hurdleRace(4, [1,6,3,5,2]))