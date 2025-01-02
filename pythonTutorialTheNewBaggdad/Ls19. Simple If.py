def main():
    Age = input("Input Your Age ")
    if int(Age) >= 8 and int(Age) <= 10:
        print("You're a Kid")
    elif int(Age) >= 11 and int(Age) <= 15:
        print("You're a Young Teen")
    elif int(Age) >= 16 and int(Age) <= 18:
        print("You're a Teenager")
    elif int(Age) >= 19 and int(Age) <= 25:
        print("You're a Young Adult")
    elif int(Age) >= 26 and int(Age) <= 40:
        print("You're an Adult")
    else:
        print("Out Of Range")
    print("Thank You!")
"""
Simplification of the functions
elif int(Age) >= 26 and int(Age) <= 40:
to
elif 26 <= int(Age) <= 40:
"""

if __name__ == '__main__':
    main()
