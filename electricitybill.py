unit=int(input("Enter the number of units consumed: "))
bill=0
if unit<=199:
    bill=unit*1.20
elif unit<400:
    bill=unit*1.50
elif unit<600:
    bill=unit*1.80
else:
    bill=unit*2.00
if bill>400:
    bill+=bill*0.15
if bill<100:
    bill=100
print(f"total bill amount: {bill:.2f}")