'''

a = 0
b = 0
print('a', 'b')
while a < 4:
    a = a + 1
    b = 0
    while b < 4:
        b = b + 1
        print(a, b)

'''

'''
Same but in For

print('a', 'b')
for a in range(1, 5):
    for b in range(1, 5):
        print(a, b)

'''

'''
#Range

print(list(range(20)))
#from 0 to 19

print(list(range(5, 20)))
#from 5 to 19

print(list(range(5, 20, 2)))
#from 5 to 19 two numbers in a time


'''
