

def main():
    ages = (20, 60, 80, 15, 45, 26, 75, 95, 35, 45, 25, 65, 67, 24, 87, 59, 33, 16, 18, 49, 69)
    ''  '# ages(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)'
    'not (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)'
    print(ages, type(ages))
    ''  '#The Tuple is immutable item, so you cant change the values unless you do the def: again'
    print(ages[5])
    ''  '# 5th Item'
    print(ages[3])
    ''  '# 3rd Item'
    print(ages[0:2])
    ''  '#The ":" goes as number of indexes, what after is isnt included'
 

if __name__ == '__main__':
    main()
