
# Step 1: Take input from the user
word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

# Step 2: Remove spaces (if any) and convert to lowercase for fair comparison
word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

# Step 3: Sort the letters of each word
sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

# Step 4: Compare the sorted words
if sorted_word1 == sorted_word2:
    print("Yes, these words are anagrams!")
else:
    print("No, these words are not anagrams.")
