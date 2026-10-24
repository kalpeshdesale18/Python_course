

# Step 1: Ask the user for a number
num = int(input("Enter a number to find its factorial: "))

# Step 2: Check if the number is negative
if num < 0:
    print(" Sorry, factorial does not exist for negative numbers.")
elif num == 0 or num == 1:
    print(f" The factorial of {num} is 1.")
else:
    # Step 3: Calculate factorial using a loop
    factorial = 1
    for i in range(2, num + 1):
        factorial *= i
    print(f" The factorial of {num} is {factorial}.")
