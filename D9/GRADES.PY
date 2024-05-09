student_scores = {"harry": 81, "ron": 78, "Hermione": 99, "Draco": 74, "Neville": 62, }
students_grades = {}

for i in student_scores:
    if student_scores[i] >= 91:
        students_grades[i]="outstanding"

    elif student_scores[i] >= 81:
        students_grades[i]="exceeds expectations"

    elif student_scores[i] >= 71:
        students_grades[i]="acceptable"

    elif student_scores[i] <= 70:
        students_grades[i]="failed"

print(student_scores)
print(students_grades)
