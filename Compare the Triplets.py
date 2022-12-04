def compareTriplets(a, b):
    alice=0
    bob = 0
    # Write your code here
    [((alice := alice+1) if a[i]>b[i] else (bob:=bob+1)) for i in range(len(b)) if a[i] != b[i]]
    return [alice, bob]
a = [1, 2, 3]
b = [3, 3, 1]
print(compareTriplets(a,b))