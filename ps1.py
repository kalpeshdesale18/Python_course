a = [12, 45, 23, 67, 45, 34]

largest = a[0]
second = None

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i != largest:
        if second == None or i > second:
            second = i

if second == None:
    print("Second largest does not exist")
else:
    print("Second largest:", second)
