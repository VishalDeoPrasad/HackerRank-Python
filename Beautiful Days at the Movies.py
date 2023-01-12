def reverseNo(num):
    return int(str(num)[::-1])

def beautifulDays(i, j, k):
    # Write your code here
    cnt = 0
    for num in range(i, j+1):
        diff = abs(reverseNo(num)-num)
        if diff % k == 0:
            cnt += 1
    return cnt

print(beautifulDays(20, 23, 6))

