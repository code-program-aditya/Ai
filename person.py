class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
    def display_info(self):
        super().display_info()
        print(f"Marks: {self.marks}")
        print(f"average marks: {self.calculate_average():.2f}")
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks) / len(self.marks)
# Example usage
student = Student("Alice", 20, [85, 90, 78])
student.display_info()