def add(a,b):
    result=a+b
    print("sum",result)
add(5,7)
#others
def add(a,b):
    s=a+b
    return(s)
k=add(5,7)
print("add:",k)
#positve and negative
def check(n):
    if n>0:
        return "positive"
    elif n<0:
        return "negative"
    else:
        return "zero"
check(-1)