
# Step 1: Get input from the user
data = input("Enter a word or number: ")

# Step 2: Convert to lowercase (for words), and remove spaces if needed
cleaned = data.lower().replace(" ", "")

# Step 3: Reverse the input
reversed_data = cleaned[::-1]

# Step 4: Compare original with reversed
if cleaned == reversed_data:
    print(" Yes! It's a palindrome.")
else:
    print(" No, it's not a palindrome.")
