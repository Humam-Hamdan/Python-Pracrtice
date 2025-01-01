class Game():


    def __init__(self):
        print('Welcome in the full game')
        print('press [1] to play Average Game')
        print('press [2] to play Even Odd Game')
        print('press [3] to play Multiplication Table Game')
        self.Choice()

    def Choice(self):
        while True:
            choice1 = input('what game you eant to play')
            try:
                choice1 = int(choice1)
                if choice1 == 1:
                    self.Average_Game()
                elif choice1 == 2:
                    self.Even_Odd_Game()
                elif choice1 ==3:
                    self.Multiplication_Game()
                else:
                    print('chose from 1, 2 or 3')
            except ValueError:
                print('enter a valid value')
        


    def Average_Game(self):
        print('this game will take several numbers from you and will retern the average of them')
        Count = int(input('How many number do you want:'))
        Current_Count = 0
        Summ = 0
        while Current_Count < Count:
            Number = float(input('Enter The Number: '))
            Summ += Number 
            Current_Count +=1
        print('sum of all numbers = ', Summ)
        print("Average of all numbers = ", Summ/Count)


    def Even_Odd_Game(self):        
        print("Welcome The Even-Odd Game \n Give Me A Number And I'll Tell You Whether It's Even or Odd"
            "\n Enter x or X to Exit")
        while True:
            number = input('Give Me A Number: ')
            if number == 'x':
                print('Closing The Game')
                print('Thank You For Playing With Me')
                break
            try:
                number = int(number)
                if number % 2 == 0:
                    print('This Number Is Even')
                else:
                    print('This Number Is Odd')
            except ValueError:
                print('Please Enter A Valid Number')
            print('-------------------------------------')


    def Multiplication_Game(self):
        print('Welcome in Multiplication Table')
        print('please enter the first and last number of the table you want')
        a = int(input('starting number: '))
        b = int(input('ending number'))
        for x in range(a, b+1):
            print('--------------------------------')
            for y in range(1, 13):
                print(x, 'X', y, ' = ', x*y)
game1 = Game()
