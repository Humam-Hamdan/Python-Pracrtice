# One

def su1(x, y):
    result = x + y

    print(result)


su1(4, 5)


# Two


def su2(x1, y1):
    global result1
    result1 = x1 + y1
    print(result1)
    return


su2(y1=int(input('y = ')), x1=int(input('x = ')))

# Three


def su3(x2=0, y2=10):

    if x2 >= y2:
        print('Try Again')
    else:
        for r in range(x2+1, y2+1):
            print(r)


su3(4)
su3(x2=int(input('x = ')), y2=int(input('y = ')))
