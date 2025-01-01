# anonymous function
summ = lambda x, y: x + y

print('total: ', summ(10, 50))


# return
def summ1(x1, y1):
    total = x1 + y1
    print('inside the function:', total)
    return total


total = summ1(20, 63)
print('outside: ', total)

# Local Vs Global
f = 0


def testt():
    f = 7
    # put "global [var] before it to be global variable
    print(f)


testt()
print(f)
