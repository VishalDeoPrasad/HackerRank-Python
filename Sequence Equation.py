def permutationEquation(p):
    return [p.index(p.index(i)+1)+1 for i in range(1, len(p)+1)]

print(permutationEquation([5,2,1,3,4]))