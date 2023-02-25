def toys(w):
    w.sort()
    curr_min = w[0]
    cnt = 1
    for i in range(len(w)):
        if w[i] > curr_min+4:
            cnt += 1
            curr_min = w[i]
    return cnt

print(toys([1,2,3,21,7,12,14,21]))