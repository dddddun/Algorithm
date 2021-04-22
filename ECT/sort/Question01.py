def solution():
    n = int(input())
    students = []
    for _ in range(n):
        students.append(list(input().split()))

    sort_student = sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for student in sort_student:
        print(student[0])


solution()