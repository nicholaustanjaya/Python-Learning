scores = [95, 82, 67, 74, 90, 88, 59, 78, 84]
Grades = []
for score in scores:
    if score>=90:
        Grades.append("A")
    elif score>=80:
        Grades.append("B")
    elif score>=70:
        Grades.append("C")
    else:
        Grades.append("F")
Total_Grades = {}
for Grade in Grades:
    if Grade in Total_Grades:
        Total_Grades[Grade]+=1
    else:
        Total_Grades[Grade]=1
print(Total_Grades)