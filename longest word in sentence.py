 
# Step 1: Get input from the user
sentence = input("Enter a sentence: ")

# Step 2: Split the sentence into words
words = sentence.split()

# Step 3: Assume the first word is the longest
longest = words[0]

# Step 4: Check every word and compare its length
for word in words:
    if len(word) > len(longest):
        longest = word

# Step 5: Print the result
print(f" The longest word is: '{longest}' with length {len(longest)}")
