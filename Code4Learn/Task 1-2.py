#1-2

print('Task 1-2')
a = int(input('Enter Starting Number: '))
b = int(input('Enter End Number: '))

b += 1
for x in range(a, b):
    print(x, 'Results')
    for y in range(a, b):
        z = y * x
        print(x, '*', y, '=', z)
