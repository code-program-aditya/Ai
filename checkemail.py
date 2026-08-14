email=str(input("Enter your email: "))
if email.count("@")==1 and email.endswith(".com"):
    print("Valid email")
else:
    print("Invalid email")
