a = [1, 2, 5, 3, 4, 6, 2, 8]

current = 1
longest = 1

for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        current += 1
    else:
        current = 1

    if current > longest:
        longest = current

print("Longest increasing section length:", longest)
