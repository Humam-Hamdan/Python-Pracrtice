"""
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
"""
if __name__ == '__main__':
    n = int(input())
    x = 1
    for n1 in range(1, n+1):
        print(x, end='')
        x += 1