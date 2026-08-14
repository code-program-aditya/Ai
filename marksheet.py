class students:
    def __init__(self, name, rollno, mark, mark_total, percentage):
        self.name = name
        self.rollno = rollno
        self.mark = mark
        self.mark_total = sum(mark_total)
        self.percentage = (self.mark_total / sum(mark_total)) * 100
    def display(self):
        print("Name :", self.name)
        print("Rollno :", self.rollno)
        print("Mark :", self.mark)
        print("Mark Total :", self.mark_total)
        print("Percentage :", self.percentage)
m = students("satyarth", "1234", 500, [100, 100, 90, 100, 100], 0)
m.display()