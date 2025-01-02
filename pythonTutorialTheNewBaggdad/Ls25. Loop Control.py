def main():
    Word = "Python"
    for Letter in Word:
        if Letter == 't':
            pass
            print("Block Is Passed")
        print(Letter)
    print("End")


if __name__ == '__main__':
    main()


"""
To Pass The "t"
Word = "Python"

    for Letter in Word:

        if Letter == 't':
            continue
            #go back to "for" and don't do the next line
        print(Letter)
    print("End")"""
"""
#Stop If "t" Appeared
Word = "Python"

    for Letter in Word:
        print(Letter)

        if (Letter == 't'):
            break
    print("End")
"""
