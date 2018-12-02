
"""print this pattern
      *
     **
    ***
   ****

"""
"""n=4
for i in range(n):
	for j in range(n):
		if i+j>=n-1:
			print "#"
		else:
			print " """


"""n=4
for i in range(n):
    #print('{:>{len}}'.format('#'*(i+1), len=n))
    print('{:>4}'.format('*'*(i+1)))
 """

n=input("Enter Number to Stairs:")
for i in range(1,n+1):
    print " "*(n-i) + "#"*i




