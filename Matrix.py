#The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

def py():
	arr1=[[1,2,3],[4,5,6],[6,7,8]]
	arr=[[-1,1,-7,-8,1],[-10,-8,-5,-2,1],[0,9,7,-1,2],[4,4,-2,1,3],[4,4,-2,1,3]]
	diog1=0
	diog2=0

	for i in range(len(arr)):
		for j in range(len(arr[0])):
			if i==j:
				diog1+=arr[i][j]
			if i+j==(len(arr[0])-1):
				diog2+=arr[i][j]
	abs_diff = abs(diog1-diog2);
			
	return abs_diff	
								
	

print py()

"""arr=[[1,2,3],[4,5,6],[6,7,8]]
numrows = len(arr)
numcols = len(arr[0])
print numrows,numcols
"""

"""

-1   1 -7 -8  1   
-10 -8 -5 -2  1
 0   9  7 -1  2
 4   4 -2  1  3
 4   4 -2  1  3
 """

"""
 00 01 02 03
 10 11 10 13
 20 21 22 23 
 30 31 32 33
 """