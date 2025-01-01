def Average():

    Count = int(input('How many number do you want:'))

    Current_Count = 0

    Summ = 0

    while Current_Count < Count:
        # print(Current_Count)
        Number = float(input('Enter The Number: '))
        Summ += Number 
        Current_Count +=1
    print("Average of all numbers = ", Summ/Count)
x = Average()


"""
 Count = int(input('How many number do you want:'))
    Numbs = [input('what the numbers are: ')]
    Numbs.sort()
    Num = sum(Numbs)
    x = 0
    for i in range(Count):
        y = x + Numbs
        print(y)
    Game = Average(self=)
"""