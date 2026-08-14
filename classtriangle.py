class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
t = triangle(10, 5)
print("Area of triangle is :", t.area())