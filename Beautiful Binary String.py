def beautifulBinaryString(b):
    # Write your code here
    b = list(b)
    cnt = 0
    for i in range(len(b)-2):
        if b[i]+b[i+1]+b[i+2] == "010":
            cnt += 1
            b[i+2] =  '1'   
    return cnt

print(beautifulBinaryString("0101010"))