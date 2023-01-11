def angryProfessor(k, a):
    # Write your code here
    early_comer = 0
    [early_comer := early_comer+1 for stu in a if stu <= 0] 
    return "NO" if early_comer >= k else "YES"

print(angryProfessor(3, [-2,-1,0,1,2]))
