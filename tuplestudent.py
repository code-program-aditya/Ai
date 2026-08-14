name=str(input("enter name:"))
rollno=str(input("enter rollno:"))
marks=int(input("enter marks:"))
student=(name,rollno,marks)
print(student)
Displaygrade=""
if marks>=90:
    displaygrade="A"
elif marks>=80:
    displaygrade="B"
elif marks>=70:
    displaygrade="C"
elif marks>=60:
    displaygrade="D"
elif marks>=50:
    displaygrade="E"
else:
    displaygrade="F"
print("grade is:",Displaygrade)