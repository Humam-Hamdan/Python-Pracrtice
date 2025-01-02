''' make the user enter the number of values he wants, automated starting from the number
the user gives you
then store the index 4 in a var and print it'''
# 3
Nums = int(input('How Many Numbers Do You Want? '))
Starting_Number = int(input('start at what number? '))
x = Starting_Number
x1 = []
while Nums > 0:
    x1.append(x)
    x += 1
    Nums -= 1
print(x1)
