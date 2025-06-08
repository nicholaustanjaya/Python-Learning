students_count = int(input("Please enter the number of students: "))

with open("scores.txt", "w") as file:
    for i in range(students_count):
        name = input(f"Enter student #{i+1} name: ")
        score = input(f"Enter score #{i+1}: ")
        file.write(name + "," + score + "\n")

students_score = {}
with open("scores.txt", "r") as file:
    for line in file:
        name, score = line.strip().split(",")
        students_score[name] = int(score)

students_grade = {}
total_score = 0
for name, score in students_score.items():
    total_score += score
    if score >= 90:
        students_grade[name] = "A"
    elif score >= 80:
        students_grade[name] = "B"
    elif score >= 70:
        students_grade[name] = "C"
    else:
        students_grade[name] = "F"

average = total_score / students_count
print(f"Average score: {average}")
print("Grades per student:", students_grade)

total_grades = {}
for grade in students_grade.values():
    if grade in total_grades:
        total_grades[grade] += 1
    else:
        total_grades[grade] = 1

print("Grade distribution:", total_grades)
