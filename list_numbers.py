list = []
num = int(input('How many numbers:'))

for x in range(num):
    number=int(input('Enter number:'))
list.append(number)
print(list)
print('Maximum in data:',max(list))
print('Minimum in data:',min(list))
print('Sum of elements in data:',sum(list))
print('Average of elements in data:',sum(list)/len(list))
