def nonDivisibleSubset(k, s):
    counts = [0]*k
    for number in s:
        counts[number % k] += 1
    count = min(counts[0], 1)
    for i in range(1, (k//2)+1):
        if i != k-i:
            count += max(counts[i], counts[k-i])
        else:
            count += 1
    return count
   
print(nonDivisibleSubset(4, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))