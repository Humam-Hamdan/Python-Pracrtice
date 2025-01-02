print(0b1010)


def f(n): print('{:08b}'.format(n))


print(f(0b1010))
print(f(0b00101))
print(0b00101)

''  '# this was for the binary'

print(0xaa)
print(f(0xaa))

''  '# this was for the hexa'

x = 0b101
y = 0b111
print(x, y)
print(x & y)
print(f(x & y))
''  '# this is how you do the "and" in bit algebra, bit by bit'
print(f(0b111 & 0b000))
print(f(x | y))
''  '#this is how you do the "or"'
print(f(0b111 >> 2))
''  '#this is how you can make it go to the right'
print(f(0b101 << 2))
''  '#this is how you can make it go to the left'
print(f(~0b111))
''  '# this is how you do the "no" or "neg" '
