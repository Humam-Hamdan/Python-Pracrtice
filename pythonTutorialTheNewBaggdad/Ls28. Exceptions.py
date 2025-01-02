def main():
    try:
        ReadFile = open("Ls27. File.txt", "r")
        for Line in ReadFile:
            print(Line)
        ReadFile.close()
    except IOError:
        print('\nFile Not Found')
    else:
        print('\nRead!')


if __name__ == '__main__':
    main()
