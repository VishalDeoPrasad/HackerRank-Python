def circularArrayRotation1(a, k, queries):
    # Write your code here
    k = k%len(a)
    last_elm = a[-k:]
    first_elm = a[:-k]
    new_a = last_elm + first_elm
    query_list = []
    for i in queries:
        query_list.append(new_a[i])
    return query_list

def circularArrayRotation2(a, k, queries):
    # Write your code here
    k = k%len(a)
    new_a = a[-k:] + a[:-k]
    return [new_a[i] for i in queries]

def circularArrayRotation(a, k, queries):
    # Write your code here
    #k = k%len(a)
    #new_a = a[-(k%len(a)):] + a[:-(k%len(a))]
    return [(a[-(k%len(a)):] + a[:-(k%len(a))])[i] for i in queries]
        
    

print(circularArrayRotation([3,4,5], 1, [1,2]))