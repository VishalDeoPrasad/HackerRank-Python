def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):     

            if i < j:
                #print(ar[i]+ar[j]%k, end=" ")
                #print((i,j), end = " ")
                if (ar[i]+ar[j])%k == 0:  
                    #print("I am here")
                    count += 1   
    return count        

print(divisibleSumPairs(6,3, [1, 3, 2, 6, 1, 2]))
