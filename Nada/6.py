'''
- كيف يمكنك عمل برنامج يقوم ب ادخال عدة قيم داخل ليست بحيث تكون كل قيمة مرتبة ابجديا 
'''
x = []
z = int(input('how many values you want to enter: '))
while z > 0:

    y = input('enter value: ')
    x.append(y)
    x.sort()
    z -= 1
print(x)
