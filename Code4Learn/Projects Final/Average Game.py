print('this game will take several numbers from you and will retern the average of them')


Count = int(input('How many number do you want:'))

Current_Count = 0

Summ = 0

while Current_Count < Count:
    # print(Current_Count)
    Number = float(input('Enter The Number: '))
    Summ += Number 
    Current_Count +=1

print('sum of all numbers = ', Summ)
# print(type(Summ))
print("Average of all numbers = ", Summ/Count)
