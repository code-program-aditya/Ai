num=input("Enter a number: ")
if "." in num:
    print("Please enter an validate integer.")
else:
    num=int(num)
    if num%2==0:
        print("the number is even")
    else:
        print("the number is odd")