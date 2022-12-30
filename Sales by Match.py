def sockMerchant(n, ar):
    # Write your code here
    cnt = 1
    pair = 0
    ar.sort()
    print(ar)
    for i in range(n-1):
        if ar[i] == ar[i+1]:
            cnt += 1
        else:
            pair += int(cnt/2)
            #print(pair)
            cnt = 1
        if i == n-2:
            pair += int(cnt/2)
    return pair

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
print(sockMerchant(n, ar))