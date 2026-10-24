
# Step 1: Input list from the user
items = input("Enter elements separated by space: ").split()

# Step 2: Create a new list without duplicates
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

# Step 3: Display the result
print(" List without duplicates:", unique_items)
