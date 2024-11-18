grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gpa = {}
students = sorted(students)
index = 0
while index < len(students):
    student = students[index]
    grade = grades[index]
    gpa[student] = sum(grade) / len(grade)
    index += 1
print(gpa)




