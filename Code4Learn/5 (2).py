class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self):
        return self.a + self.b

    def Multi(self):
        return self.a * self.b

class Scientific(Calculator):
    def Power(self):
        return self.a ** self.b


x = Scientific(3, 5)

print(x.Add, x.Multi, x.Power)
