n = int(input())

student_grades = {}

for _ in range(n):
    name, grade_as_string = tuple(input().split())
    grade = float(grade_as_string)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)

for name, every_grade in student_grades.items():
    average_grad = sum(every_grade) / len(every_grade)
    formatted_grades = f"{' '.join([f'{gr:.2f}' for gr in every_grade])}"
    print(f"{name} -> {formatted_grades} (avg: {average_grad:.2f})")



count = int(input())
students = {}
for _ in range(count):
    line = tuple(input().split())
    student, grade = line

    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for name, every_grade in students.items():
    average_grad = sum(every_grade) / len(every_grade)
    formatted_grades = f"{' '.join([f'{gr:.2f}' for gr in every_grade])}"
    print(f"{name} -> {formatted_grades} (avg: {average_grad:.2f})")