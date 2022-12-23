def getTotalX(a, b):
    multiple_factor_list = []
    final_list = []
    n = len(a)+len(b)
    [multiple_factor_list.append(i) for num in a for i in range(num, b[0]+1, num)]
    
    [multiple_factor_list.append(i) for num in b for i in range(1, b[0]+1) if num%i == 0]
    
    unique = set(multiple_factor_list)
    [final_list.append(i) for i in unique if multiple_factor_list.count(i) == n]
            
    #return multiple_factor_list, final_list
    return len(final_list)

print(getTotalX([2,6], [24,36]))
        