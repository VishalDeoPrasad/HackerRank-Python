def gemstones(arr):
    comm = set(arr[0])
    for i in range(1, len(arr)):
        comm = comm.intersection(set(arr[i]))
    return len(comm)
arr = ['abcdde', 'baccd', 'eeabg']
print(gemstones(arr))