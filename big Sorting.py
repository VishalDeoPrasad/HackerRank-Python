def bigSorting(unsorted):
    # Write your code here
    return sorted(unsorted, key = lambda s: int(s))
ar = ['1', '200', 3, '5']
print(bigSorting(ar))