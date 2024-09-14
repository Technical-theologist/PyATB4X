class Calc:
    def __init__(self, a, b):  # you are passing the parameter
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


result = Calc(10, 20)
x = result.mul()
print(x)


class person:
    name = "Amit"  # This value is hardcoded thus why we need the constructor

    def walk(self, name):
        print(self.name)


xyz = person()
pramod = person()
print(xyz.name)
print(xyz.name)


class person_1:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(self.name)


abc = person_1("Amit1")
print(abc.name)
