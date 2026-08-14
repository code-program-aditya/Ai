#global variable
a=10
def fun1():
    print("global: ", a)
def fun2():
    print("global: ", a)
    print("local: ", a)
fun1()
fun2()
#local variable
def fun3():
    a=700
    print("local: ", a)
fun3()
def fun4():
    print("global: ", a)
fun4()