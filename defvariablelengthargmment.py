#variable length arguments
def sum(t,*n):
    print("temp :",t)
    s=0
    for i in n:
        s=s+i
    print("sum :",s)
sum(100)
sum(10,20)
sum(10,20,30)
sum(10,20,30,40)