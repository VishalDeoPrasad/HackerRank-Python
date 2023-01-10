def utopianTree1(n):
    # Write your code here
    height = 0
    for i in range(n+1):
        if i%2 == 1:
            height = height*2
        else:
            height += 1
    return height

def utopianTree(n):
    # Write your code here
    height = 0
    [height := height*2 if i%2 == 1 else height+1 for i in range(n+1)]          
    return height

print(utopianTree(4))
