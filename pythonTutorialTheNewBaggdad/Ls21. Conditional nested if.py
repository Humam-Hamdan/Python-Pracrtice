def main():
    degree = input("Enter Your degree: ")
    if int(degree) >= 90:
        if int(degree) > 94:
            print("Your Evaluation is: A+")
        else:
            print("Your Evaluation is: A-")
    elif 80 <= int(degree) <= 89:
        print("Your Evaluation is: B")
    elif 70 <= int(degree) <= 79:
        print("Your Evaluation is: C")
    elif 60 <= int(degree) <= 69:
        print("Your Evaluation is: D")
    elif 50 <= int(degree) <= 59:
        print("Your Evaluation is: E")
    else:
        print("You Failed")

if __name__ == '__main__':
    main()
