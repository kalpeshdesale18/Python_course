 

# Step 1: Take input from the user
num = int(input("Enter a number: "))

# Step 2: Check basic cases
if num <= 1:
    print(" Not a prime number (must be greater than 1).")
else:
    is_prime = True  # We assume it's prime until we find a factor

    # Step 3: Try dividing num by all numbers from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # No need to check further

    # Step 4: Print the result
    if is_prime:
        print(f" Yes, {num} is a prime number.")
    else:
        print(f" No, {num} is not a prime number.")











