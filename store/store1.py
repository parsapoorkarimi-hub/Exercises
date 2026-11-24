import re

Products = {
    's26 ultra 512 G' : {
        'price' : 300,
        'stock' : 30
    },
    's26 ultra 256 G' : {
        'price' : 250,
        'stock' : 35
    },
    'iphone 17 pro max 512 G' : {
        'price' : 400,
        'stock' : 20
    },
    'iphone 17 pro max 256 G' : {
        'price' : 350,
        'stock' : 25
    }
}

class SignUp:
    def __init__(self, name, lname, age, password, email):
        self.name = name
        self.lname = lname
        self.age = age
        self.p1 = password
        self.email1 = email
        self.cart = {}
        self.order_history = []
        

    def checkemail(self):
        while not re.fullmatch(r"^[\w.-]+@[\w.-]+\.\w{2,}$", self.email1):
            print('The entered email is incorrect.')
            self.email1 = input('Enter your email again: ')

    def checkp(self):
        while not self.p1.isdigit() or len(self.p1) < 8:
            print('The entered password is incorrect.')
            self.p1 = input('Enter your password again: ')

    def Show(self):
         
         for number, (name , info) in enumerate(Products.items() , start= 1):
            print(f"{number}. Product Name: {name} | price: {info['price']} | stock: {info['stock']}")   # You can use Enter.

         print(f"{len(Products) + 1}. Finish shopping")

    def _get_int(self, message):
      while True:
        try:
            return int(input(message))
        except ValueError:
            print('Please enter a valid number.')

    def Add(self):

        self.Show()
        choice = self._get_int('Select the desired option: ')

        if choice == len(Products) + 1:
            return 
        
        if not 1 <= choice <= len(Products):
             print('Invalid option.')
             return
        
        name, info = list(Products.items())[choice - 1]

        self.Add_product(name, info)

    def Add_product(self , name , info):

        already_in_cart = self.cart.get(name, {}).get('Quantity', 0)

        available = info['stock'] - already_in_cart

        if available <= 0:
            print('No more stock available.')
            return

        x = self._get_int('How much of the product do you want? ')  

        while x < 0 or x > available:
            print(f'The available quantity is {available}.')
            print('By pressing the zero button, you return to the previous page.')
            x = self._get_int('Enter the quantity again: ')

        if x == 0:
           print('You will return to the previous menu.')
           return

        y = x * info['price']
        
        if name in self.cart:
          self.cart[name]['Quantity'] += x
          self.cart[name]['Total product price'] += y
        else:
          self.cart[name] = {
                 'Quantity': x,
                'Total product price': y
                   }
                 
        print('Added to your shopping cart')

    def Remove(self):
       while True:

        if not self.cart:
           print('Your shopping cart is empty.')
           return

        s = list(self.cart.keys())
        
        for number , name in enumerate(s , start=1):
            print(f"{number}. {name} | Quantity: {self.cart[name]['Quantity']}")

        print(f"{len(s) + 1}. exit")

        r = self._get_int('Which product do you want to remove? ')

        if r == len(s) + 1:
           return
 
        if not 1 <= r <= len(s):
              print('Invalid option.')
              continue
             
        N = s[r - 1]
        H = self._get_int('How much of this product are you removing?')

        while H > self.cart[N]['Quantity'] or H <= 0:
         print('The entered quantity is incorrect.')
         H = self._get_int('Enter the quantity again:')
         

        self.cart[N]['Quantity'] -= H

        d = Products[N]['price'] * self.cart[N]['Quantity']
        self.cart[N]['Total product price'] = d

        if self.cart[N]['Quantity'] == 0:
          del self.cart[N]

        print('The requested number of items has been deleted.')

    def View(self):
       
       if not self.cart:
            print('Your shopping cart is empty.')
            return
       
       for name, info in self.cart.items():
          print(name)
          for key, value in info.items():
            print(f'{key} : {value}')

       Grand = 0
       for x in self.cart.values():
         Grand += x['Total product price']

       print(f'\nGrand Total: ${Grand}')

    def complete(self):
       
       if not self.cart:
            print('Your shopping cart is empty.')
            return

       S = sum(
                   info['Total product price']
                   for info in self.cart.values()
               )
       
       print(f'The amount you need to pay: $ {S}')

       while True:
         P = self._get_int('Are you paying? 1. Yes  2. No')

         if P == 1:
           break

         elif P == 2:
                   print('Not paid')
                   print('You are returning to the main page.')
                   return
         else:
            print('Invalid option. please try again.')

       for name, info in self.cart.items():
            if info['Quantity'] > Products[name]['stock']:
                 print(f'Insufficient stock for {name}')
                 return
            
       order = {}
       for name, info in self.cart.items():
           order[name] = info.copy()

       for name, info in self.cart.items():
            Products[name]['stock'] -= info['Quantity']

       self.order_history.append(order)

       self.cart.clear()

       print('Paid successfully.')
       print('Your order has been registered.')
          
    def order(self):

       if not self.order_history:
            print('You have no previous orders.')
            return
       
       for number, Order in enumerate(self.order_history, start=1):
            print(f'\n---------- Order {number} ----------')
            total = 0
            for name, info in Order.items():
             print(name)
             for key, value in info.items():
              print(f'{key}: {value}')
              total += info['Total product price']

       print(f'Order Total: ${total}')

    def search(self):
       
       R = input('Your search: ').strip()

       if not R:
            print('Please enter a search term.')
            return
       
       results = []

       for name, info in Products.items():
            if re.search(re.escape(R), name, flags=re.IGNORECASE):
                results.append((name, info))

       if not results:
            print('No products found.')
            return
       
       for number, (name, info) in enumerate(results, start=1):    
         print(f"{number}. Product Name: {name} | price: {info['price']} | stock: {info['stock']}")
               

       print(f'{len(results) + 1}. Exit')

       w = self._get_int('Select your product: ')

       if w == len(results) + 1:
            return
       
       if not 1 <= w <= len(results):
            print('Invalid option.')
            return
       
       name, info = results[w - 1]

       self.Add_product(name, info)

    def run(self):
        self.checkemail()
        self.checkp()
        return self.email1 , self.p1

class Store:
    def __init__(self):
        self.users = []

    




    


