#object oriented programming using python
#class : properties
class student:
    def __init__(self):
        self.mark = "500"
        self.rollno = "1234"
        self.name = "satyarth"
    def show(self):
        print("Hello my mark is :",self.mark)
        print("My rollno is :", self.rollno)
        print("my name is :", self.name)
s=student()
s.show()
# scond
class students:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def __dict__(self):
        return {
            "name": self.name,
            "rollno": self.rollno,
            "marks": self.marks
        }