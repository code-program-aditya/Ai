deptA = set(str(input("enter the name of workshop of department A: ")).split(','))
n1 = int(input("Enter number of students in Department A workshop: "))
for i in range(n1):
    sid = input(f"Enter student ID {i+1} for Department A: ")
    deptA.add(sid)
deptB = set(str(input("enter the name of workshop of department B: ")).split(','))
n2 = int(input("Enter number of students in Department B workshop: "))
for i in range(n2):
    sid = input(f"Enter student ID {i+1} for Department B: ")
    deptB.add(sid)
both = deptA.intersection(deptB)
print("Students who attended both workshops:")
if both:
    for sid in both:
        print(sid)
else:
    print("No student attended both workshops.")