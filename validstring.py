s=str(input("Enter username: "))
if s.isalnum() and not s[0].isdigit() and len(s)>=6 and len(s)<=12:
    print("Valid username")
else:
    print("Invalid username")