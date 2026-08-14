def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

num = list(int(x) for x in input("Enter numbers separated by commas: ").split(','))
for n in num:
    if is_prime(n):
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")