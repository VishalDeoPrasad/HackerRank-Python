def simpleArraySum(ar):
	ArraySum = 0
	[ArraySum := ArraySum + i for i in ar]
	return ArraySum

print(simpleArraySum([1,2,3]))