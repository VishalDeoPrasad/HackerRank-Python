def birthdayCakeCandles(ar):
	max_num=max(ar)
	large=0
	for item in ar:
		if max_num==item:
			large+=1
		
	return large

ar=[2,3,1,5,5,6,6]
print birthdayCakeCandles(ar)