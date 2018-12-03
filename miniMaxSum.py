def miniMaxSum(arr):
	num_sum=sum(arr)
	num_min=min(arr)
	num_max=max(arr)
	mini=num_sum - num_max
	maxi=num_sum - num_min
	print mini,maxi

arr=[3245,5674,21,123,567576]
miniMaxSum(arr)
