def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            next_multiple = 5 - grades[i]%5
            if next_multiple < 3:
                grades[i] = grades[i] + next_multiple

    return grades


new_grades = gradingStudents([73, 67, 38, 33])
print(new_grades)
