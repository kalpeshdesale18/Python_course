a = [2, 4, 5, 1, 9, 11, 15]
prime = []
non_prime = []

for i in a:
    count = 0

    if i >= 2:
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

    if count == 2:
        prime.append(i)
    else:
        non_prime.append(i)

print("Prime numbers:", prime)
print("Non-prime numbers:", non_prime)
