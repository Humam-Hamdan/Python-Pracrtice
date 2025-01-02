def main():
    ReadFile = open("Ls27. File.txt", "r")
    for Line in ReadFile:
        print(Line)
    ReadFile.close()


if __name__ == '__main__':
    main()

"""
How To Create And Add Files
def main():
    Out = open("Ls27. File.txt", "w")
    Out.write("Hello")
    Out.close()


if __name__ == '__main__':
    main()
"""
"""
How To Append Text in Files
def main():
    Out = open("Ls27. File.txt", "a")
    Out.write("\nName = Hud")
    Out.write("\nName = Nad")
    Out.write("\nName = Serf")
    Out.write("\nName = Sans")
    Out.write("\nName = Ari")
    Out.write("\nName = Mari")
    Out.close()


if __name__ == '__main__':
    main()

"""
"""
How to Read text
def main():
    ReadFile = open("Ls27. File.txt", "r")
    for Line in ReadFile:
        print(Line)
    ReadFile.close()


if __name__ == '__main__':
    main()
"""