  

# Step 1: Take input from the user
text = input("Enter a string to compress: ")

# Step 2: Initialize variables
compressed = ""
count = 1

# Step 3: Loop through the string
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1  # Same as previous character, increase count
    else:
        compressed += text[i - 1] + str(count)  # Add previous char and count
        count = 1  # Reset count

# Step 4: Add the last character group
compressed += text[-1] + str(count)

# Step 5: Return compressed string only if shorter
if len(compressed) < len(text):
    print(" Compressed String:", compressed)
else:
    print(" Compressed string is not shorter. Original String:", text)
