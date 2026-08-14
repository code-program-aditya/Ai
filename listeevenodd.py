user_list=[int(x) for x in input("Enter elements separated by space: ").split(',')]
even_list = set([num for num in user_list if num%2==0])
odd_list = set([num for num in user_list if num%2!=0])
print("Even numbers in the list:", even_list)
print("Odd numbers in the list:", odd_list)