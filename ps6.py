a = [34, 12, 89, 5, 67, 23]

largest = a[0]
smallest = a[0]

for i in a:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)