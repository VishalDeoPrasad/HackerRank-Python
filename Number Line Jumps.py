def kangaroo(x1, v1, x2, v2):
    # Write your code here
    kangaroo_1_distance = x1
    kangaroo_2_distance = x2
    i = 0 
    while i<12250:
        if kangaroo_1_distance == kangaroo_2_distance:
            return "YES"
        else:
            kangaroo_1_distance += v1
            kangaroo_2_distance += v2
        i += 1
    return "NO"

print(kangaroo(0, 2, 5, 3))