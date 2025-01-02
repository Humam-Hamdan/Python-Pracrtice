
def main():
    ages = [20, 60, 80, 15, 45, 26, 75, 95, 35, 45, 25, 65, 67, 24, 87, 59, 33, 16, 18, 49, 69]
    ''  '# ages(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)'
    'not (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)'
    ages.append(50)
    ''  '#ages.append() is how you can add things to the lists in the last index'
    ages.insert(1, 43)
    ''  '#ages.insert() is how you can add things in the index you want to add in'
    print(ages, type(ages))
    ''  '#The lists is mutable item, so you can change the values'
    print(ages[5])
    ''  '# 5th Item'
    print(ages[3])
    ''  '# 3rd Item'
    print(ages[0:3])
    ''  '#The ":" goes as number of indexes, what after is isnt included'
    data = "Software Engineer"
    print(data[0:5])


if __name__ == '__main__':
    main()
