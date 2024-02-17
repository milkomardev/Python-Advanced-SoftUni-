students = {}

for _ in range(int(input())):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)

for student, grades in students.items():
    print(f'{student} -> {" ".join(str(f"{x:.2f}") for x in grades)} (avg: {(sum(grades)/len(grades)):.2f})')