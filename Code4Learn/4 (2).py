class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self):
        return self.a + self.b

    def Multi(self):
        return self.a * self.b

Calc = Calculator(30, 70)

print(Calc.Add())

print(Calc.Multi())
