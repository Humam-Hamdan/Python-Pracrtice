
Size = int(input('How High Should I Go? '))
Size += 1
for s in range(1, Size):
    for c in range(s):
        print('*', end='')
    print()
