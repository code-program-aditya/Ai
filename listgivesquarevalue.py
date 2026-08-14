from matplotlib.pylab import square
manager_list=[20,50,44,67,89,54,45]
print("The list of numbers is:",manager_list)
print("The square of the numbers in the list is:", square(manager_list))
def square(x):
    square = []
    for i in x:
        square.append(i**2)
    return square