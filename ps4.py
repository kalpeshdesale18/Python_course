n = int(input("Enter a number: "))

temp = n
digits = 0

while temp > 0:
    digits += 1
    temp = temp // 10

temp = n
total = 0

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")