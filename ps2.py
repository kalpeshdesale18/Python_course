n = int(input("Enter a number: "))
temp = n
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if n == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")