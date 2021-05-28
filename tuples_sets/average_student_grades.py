num_lines = int(input())
student_record = {}
for i in range(num_lines):
    name, grade = input().split()
    grade = (float(grade),)
    student_record[name] = student_record.get(name, ()) + grade
for student, grades in student_record.items():
    # because we cannot unpack within a formatted string we map each element of the tuple to a string
    # using anon function we can make the stringify the float number up to 2 decimal points
    print(f'{student} -> {" ".join(map(lambda x: f"{x:.2f}", grades))} (avg:{sum(grades) / len(grades):.2f})')
