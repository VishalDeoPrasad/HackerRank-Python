def pageCount(n, p):
    # Write your code here
    front_turn = int((p/2)+1-1 if p%2 == 0 else ((p+1)/2)-1)
    back_turn = int((n-p)/2) if n%2 != 0 else int((n-p+1)/2)
    return min(front_turn, back_turn)

print(pageCount(7, 3))
