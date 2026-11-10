name = input()

li = []
total_marks=0

for i in range(1, 4):
    m = int(input())
    li.append(m)
    total_marks+=m


avg_marks = total_marks / 3

grade=""

if avg_marks >= 80 and avg_marks<=100:
    grade = "A+"
elif avg_marks >= 70 and avg_marks<=79:
    grade = "A"
elif avg_marks >= 60 and avg_marks<=69:
    grade = "B"
elif avg_marks >= 50 and avg_marks<=59:
    grade = "C"
elif avg_marks <50:
    grade = "F"

print(
    f"\nStudent Name: {name}"
    f"\nTotal Marks: {total_marks}"
    f"\nAverage: {avg_marks:.2f}"
    f"\nGrade: {grade}"
)
