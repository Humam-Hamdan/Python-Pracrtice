#1

print('Task 1')

for x in range(0, 13):
    print(x, 'Results')
    for y in range(0, 13):
        z = y * x
        print(x, '*', y, '=', z)
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
#2

print('Task 2')

for i in range(21):
    if i == 10:
        continue
    print(i)
    i += 1
#2-2

print('Task 2-2')

for i in range(21):
    if i == 10:
        break
    print(i)
    i += 1
