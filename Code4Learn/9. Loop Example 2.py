
print('This Program Displays a List Of Numbers And Their Squares')

start = int(input('Enter The Starting Number: '))

end = int(input('How High Should I Go? '))

print('Number   \t    Square')

print('---------------------')

end += 1

for i in range(start, end):

    square = i * i

    print(' ', i, '\t', '\t', '  ', square)
