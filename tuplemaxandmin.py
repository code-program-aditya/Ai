sal=(12000,55500,44000,40000,20000)
largest=max(sal)
smallest=min(sal)
print("largest salary is:",largest)
print("smallest salary is:",smallest)
secondlargest=smallest
for salary in sal:
    if salary>secondlargest and salary<largest:
        secondlargest=salary
print("second largest salary is:",secondlargest)