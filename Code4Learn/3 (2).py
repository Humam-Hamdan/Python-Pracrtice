class student:
    def __init__(self, name):
        self.name = name
        self.marks = []

        print('Welcome {} To MIoTC School!'.format(name))

    def AddMarks(self, marks):
        self.marks.append(marks)

    def AVG(self):
        return sum(self.marks)/len(self.marks)


s1 = student('Humam')

print(s1.marks)

s1.AddMarks(50)

s1.AddMarks(40)

s1.AddMarks(30)

s1.AddMarks(60)

s1.AddMarks(70)

s1.AddMarks(90)

s1.AddMarks(10)

print(s1.marks)

print(s1.AVG())
