# One
def printstr(str):
    """this is a function to print string"""

    print(str)

    return


printstr('Hello')

printstr('Humam')

printstr(str='Welcome!')

# Two


def summ(x, y):
    print(x + y)

    return


summ(3, 4)
summ(9, 45)

# Three


def printme(name, age=35):
    print('name: ', name)
    print('age: ', age)

    return


printme(age=17, name='Humam')
printme('Mahmoud')


def Usum(arg, *vartuple):
    print('OutPut')
    # print(arg)
    # print(vartuple)
    # print()
    result = arg
    for var in vartuple:
        result = result + var

    print(result)


Usum(10, 56874, 32148979, 319879, 65498765)
