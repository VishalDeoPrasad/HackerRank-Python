arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
	n=len(arr)
	pos, neg, zero = 0,0,0
	[(zero:=zero+1) if i==0 else [(pos:=pos+1) if i>0 else (neg:=neg+1)] for i in arr]
	#print(round(pos/n, 6), round(neg/n, 6), round(zero/n, 6))
	print(f'{pos/n:.6f}\n'f'{neg/n:.6f}\n'f'{zero/n:.6f}\n')

plusMinus(arr)

# for i in arr:
# 	if i==0:
# 		zero+=1
# 	else:
# 		if i>0:
# 			pos+=1
# 		else:
# 			neg+=1