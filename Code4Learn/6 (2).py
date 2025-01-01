class animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{} is eating {}'.format(self.name, food))


class dog(animal):
    def fetch(self, thing):
        print('[} get the {}'.format(self.name, thing))


class cat(animal):
    def cat_eat(self):
        print('{} is eating food'.format(self.name))
