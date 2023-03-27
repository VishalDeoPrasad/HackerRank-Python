def pageCount1(n, p):
    # Write your code here
    front_turn = int((p/2)+1-1 if p%2 == 0 else ((p+1)/2)-1)
    back_turn = int((n-p)/2) if n%2 != 0 else int((n-p+1)/2)
    return min(front_turn, back_turn)

def pageCount(n, p):
    if n%2==0:
        n = n+1
    left = p//2
    right = (n-p)//2
    return min(left, right)

print(pageCount(7, 3))
