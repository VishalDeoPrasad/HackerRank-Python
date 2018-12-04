
def gradingStudents(grades):
	marks=[]
	for i in range(len(grades)):
		if grades[i]<38:
			marks.append(grades[i])
		else:
			m1=grades[i]+1
			m2=grades[i]+2
			if m1%5==0:
				marks.append(m1)
			elif m2%5==0:
				marks.append(m2)
			else:
				marks.append(grades[i])

	return marks	
grades=[73,67,38,33]
print gradingStudents(grades)

