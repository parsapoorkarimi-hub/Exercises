class car:
    numder = 0

    def __init__(self, model, price):         #Whenever we create an object, the `init` function is called, and the code with in it is executed.
        self.model = model
        self.price = price
        self.stutus = False
        car.numder += 1

    def start(self):
        if self.stutus == False:
            print(f'{self.model} is starting')
            self.stutus = True
        else:
            print('The car had been started')

    def off(self):
        if self.stutus:
            print('car is off now')
            self.stutus = False
        else:
            print(f'{self.model} is off please start first')

print(car.numder)
car1 = car('benz','240')
car2 = car('samand','300')
car3 = car('vira', '400')
print(car.numder)

car.numder = 6       # If a change occurs in the template, it affects all objects.
car2.numder = 9      #Modifying an object affects only that object itself
print(car.numder)
print(car1.numder)
print(car2.numder)

