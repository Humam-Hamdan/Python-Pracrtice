tup1 = ('physics', 'chemistry', 1997, 2001)

print(tup1[0])

print(tup1[1:])

tup2 = (12, 34.56)

tup3 = ('abc', 'xyz')

tup4 = tup3 + tup2

print(tup4)

tup = ('physics', 'chemistry', 1997, 2001)

print(tup)

del tup

print(tup)

# tuples is immutable

L = ('spam', 'python', 'Welcome')

print(L[2], L[-2])

"""
# Methods

len()

max() , min()

##################

L = ('spam', 'python', 'Welcome')

d = list(L)

# finished editing

f = tuple(d)

"""