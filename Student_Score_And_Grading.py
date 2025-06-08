Students_Count = int(input("Please enter the number of students : "))
with open("scores.txt", "w") as file:
    for i in range(Students_Count):
        name = input(f"Enter student #{i+1} name :")
        score = input(f"Enter score #{i+1}: ")
        file.write(name + "," + score + "\n")

with open("scores.txt", "r") as file:
    lines = file.readlines()
    Students_Score = {}
    for line in lines:
        student_name_score=line.strip().split(",")
        Students_Score[student_name_score[0]] = student_name_score[1]

i=0
sum=0
Students_Grade = {}
for name, val in Students_Score.items():
   sum+=int(val)
   i+=1
   if int(val)>=90:
       Students_Grade[name]="A"
   elif int(val)>=80:
       Students_Grade[name]="B"
   elif int(val)>=70:
        Students_Grade[name] = "C"
   else:
        Students_Grade[name] = "F"
average = sum/i
print(f"Average score : {average}")
print(Students_Grade)

Total_Grades = {}
for Grade in Students_Grade.values():
    if Grade in Total_Grades:
        Total_Grades[Grade]+=1
    else:
        Total_Grades[Grade]=1
print(Total_Grades)