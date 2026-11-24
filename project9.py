document = [
    {
        'title' : 'python',
        'color': 'blue'
    },
    {
        'title' : 'HTML',
        'color' : 'red'
    }
]






class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lname = lastname

    def me(self):
        print(f'hello {self.name} {self.lname}')


class student(Person):
    def __init__(self, name, lastname, age):
        super().__init__(name, lastname)  
        self.age = age
        self.cs = []

    def welcome(self):
        print('im student')
        super().me()

    def printcs(self):
        if self.cs:                  #len(self.cs) > 0
            for x in self.cs:
                print(x['title'], x['color'])                                     
        else:
            print('itbis impossible')

s1 = student('parsa','poorkarimi',30)
s1.cs.append(document[0])
s1.cs.append(document[1])
s1.printcs()