class student:
    def __init__(self, name, marks):
     self.name=name
     self.marks=marks
    def show(self):                                       
        print("hi:" ,self.name)
        print("your marks :",self.marks)
    def grade(self):
        if self.marks>60:
            print("grade a")
        elif self.marks>50:
            print("garde b")
        else:
            print("grade c")
n=int(input("enter no of students"))
for i in range(n):
    name=input("enter the student name")
    marks=int(input("enter the marks"))
    s=student(name,marks)
    s.show()
    s.grade()