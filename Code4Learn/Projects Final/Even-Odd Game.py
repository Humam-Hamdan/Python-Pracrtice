# Even = /2
# Odd  <> /2
"""
build a simple game that takes a number from user and tell the user if this number is even or odd
# Make sure that your game include :
    If the users press x the game will exit
    If user enter not number , tell him to enter a number
    The game continue even after I get the result

"""

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