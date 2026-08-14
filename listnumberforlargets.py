# Function to find largest and second largest
def find_two_largest(numbers):
    # Sort the list in descending order
    sorted_nums = sorted(numbers, reverse=True)
    largest = sorted_nums[0]
    second_largest = sorted_nums[1] if len(sorted_nums) > 1 else None
    return largest, second_largest

# Main program
nums = []

n = int(input("Enter how many numbers: "))
for i in range(n):
    val = int(input(f"Enter number {i+1}: "))
    nums.append(val)

largest, second_largest = find_two_largest(nums)

print("\nNumbers entered:", nums)
print("Largest number:", largest)
print("Second largest number:", second_largest)