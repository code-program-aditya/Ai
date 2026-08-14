from turtle import st
from matplotlib.pylab import average
student_name=str(input("Enter the name of the student: "))
student_mark=list(map(int, input("Enter the marks of the student : ").split(',')))
print("The name of the student is:",student_name)
print("The mark of the student is:",student_mark)
print("avg mark of the student is:",average(student_mark))
def calculate_average(marks):
    marks_total = sum(marks)
    marks_count = len(marks)
    average_mark = marks_total / marks_count
    return average_mark