"""
#Simple Loop
x = 0

while x < 10:
    print(x)
    x += 1
else:
    print('x >= 10')

print('Mahmoud Ahmed')
"""
"""
#Single Line

x = 0

while x < 10 : print(x) ; x += 1
"""

# Loop Example

x = 0

while x < 5:
    y = 0
    print(x + 1, 'x interation')
    while y < 3:
        print('x = ', x, 'y = ', y)
        print(y + 1, 'y interation')
        y += 1
    x += 1
