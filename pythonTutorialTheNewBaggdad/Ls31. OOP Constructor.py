class Car:
    def __init__(self, Name):
        Name = self.Name
        print('Create Class Instance')
    def GetOwner(self):
        #Name = input('What is you name: ')
        print('Owner is ',self.Name)
    #def SetOwner(self):
    #    Name = input('What is You Name')


def main() :
    mycar=Car('Humam')
    #mycar.SetOwner('Humam Hamdan')
    mycar.GetOwner()


if __name__ == '__main__':main()
