a=str(input("enter a string: "))
upper_count=0
lower_count=0
number_count=0
specal_count=0
for s in a:
    if s.isupper():
        upper_count+=1
    elif s.islower():
        lower_count+=1
    elif s.isdigit():
        number_count+=1
    else:
        specal_count+=1
print(f"Upper case letters: {upper_count}")
print(f"Lower case letters: {lower_count}")
print(f"Digits: {number_count}")
print(f"Special characters: {specal_count}")