class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        del self.c
t=test()
print(t.__dict__)
t.m1()
print(t.__dict__)