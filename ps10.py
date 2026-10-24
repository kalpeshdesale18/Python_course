a = [2, 4, 6, 3, 7, 5]
target = 9

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target:
            print(a[i], j, a[j])
