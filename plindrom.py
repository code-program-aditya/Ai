def palindrom(s1):
    s2=s1[::-1]
    if s1==s2:
        print("palindrom")
    else:
        print("not a palindrom")
s=input("enter a string")
print(s)
palindrom(s)
