import datetime
def main():
    DOB = input("Enter Your DOB:")
    YearNow = datetime.datetime.now().year
    MyAge = YearNow - int(DOB)
    print("Your Age is {}".format(MyAge))


if __name__ == '__main__':
    main()
