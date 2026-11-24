a = int(input('enter youe number1: '))
b = int(input('enter youe number2: '))


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
       
        

    def add(self):
        print(self.a + self.b)

    def subtract(self):
        print(self.a - self.b)

    def multiply(self):
        print(self.a * self.b)

    def divide(self):
        if self.b == 0:
            print('It is impossible.')
        elif a % b == 0:
            print(int(self.a / self.b))
        else:
            print(self.a / self.b)

p = Calculator(a,b)

p.add()
p.subtract()
p.multiply()
p.divide()

