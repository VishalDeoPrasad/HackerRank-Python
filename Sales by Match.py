def sockMerchant1(n, ar):
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

def sockMerchant(n, ar):
    socks_count = {}
    for a in ar:
        if a not in socks_count:
            socks_count[a] = 1
        else:
            socks_count[a] += 1
            
    unpair = 0
    for key,val in socks_count.items():
        unpair += val%2
        
    return (n-unpair)//2

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
print(sockMerchant(n, ar))