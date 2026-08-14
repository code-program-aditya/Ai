class test:
    def m1(cls):
        cls.a=500
    def m2():
        test.a=50
t=test()
print(test.a)
#test.m1(test)
#print(test.a)
test.m2()
print(test.a)