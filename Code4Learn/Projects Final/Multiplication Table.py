print('Welcome in Multiplication Table')

print('please enter the first and last number of the table you want')

a = int(input('starting number: '))

b = int(input('ending number'))

for x in range(a, b+1):
    print('--------------------------------')
    for y in range(1, 13):
        print(x, 'X', y, ' = ', x*y)
