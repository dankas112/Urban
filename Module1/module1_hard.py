# Input Data:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Create new vars:
average_grades = []
students_grades = {}
students_index = 0
list_students = list(students)
list_students.sort()

# Calculate average grade, and insert students and their grades in the dictionary:
for x in grades:
    x = sum(x) / len(x)                         # Calculate average grade
    average_grades.append(x)                    # Insert it in the list
    student = list_students[students_index]     # Get every student
    students_grades[student] = x                # Insert student + grade in the our dict
    students_index += 1                         # Get next student

# Display result:
print(students_grades)
