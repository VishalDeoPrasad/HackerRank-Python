def aVeryBigSum(ar):
    # Write your code here
    bigSum = 0
    [bigSum := bigSum+i for i in ar]
    return bigSum
ar=[1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
print(aVeryBigSum(ar))