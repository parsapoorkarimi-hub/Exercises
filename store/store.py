from store1 import SignUp , Store
person = Store()
current_user = None

while True:
 print('1. sign up')
 print('2. login')

 try : 
     choice = int(input('Select the desired option: '))
 except:
      print('error. Enter again:')
      continue

 if choice == 1:

    name = input('Enter your name: ')
    lname = input('Enter your last name: ')
    age = input('Enter your age: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')
 
    user = SignUp( name, lname, age, password, email)
    user.run()
    person.users.append(user)

    print('Sign up was successful.')
    continue
    
 elif choice == 2:

  if not person.users:
       print('No registered users. Please sign up first.')
       continue

  email = input('Enter your email: ')

  while True:

      matched_user = None

      for user in person.users:
            if user.email1 == email:
              matched_user = user
              break

      if matched_user is None:
            print('This email is not registered.')
            email = input('Enter your email again: ')
            continue

      password = input('Enter your password: ')

      if password == matched_user.p1:
            current_user = matched_user
            print('Welcome!')
            break

      else:
            print('The password is incorrect.')

  break

 else:
       print('The selected option is incorrect.')
       
  
while True:
  print('\n1. Show Products')
  print('2. Search Products')
  print('3. View Cart')
  print('4. Complete Purchase')
  print('5. Order History')
  print('6. Exit')

  choice = current_user._get_int('Which one do you choose?')

  if choice == 1:
        current_user.Show()
        while True:
         a = current_user._get_int('Select: 1. Add Product to Cart 2. Search Products 3. exit')
        
         if a == 1:
               current_user.Add()
               break
        
         elif a == 2:
               current_user.search()
               break
        
         elif a == 3:
               break
        
         else:
            print('Invalid option. Try again.')
        
  elif choice == 2:
        current_user.search()

  elif choice == 3:
        current_user.View()
        while True :
         
         b = current_user._get_int('Select: 1. Remove Product from Cart 2. exit')

         if b == 1:
               current_user.Remove()
               break
         if b == 2:
               break
         else:
            print('Invalid option. Try again.')


  elif choice == 4:
        current_user.complete()

  elif choice == 5:
        current_user.order()

  elif choice == 6:
        print('Goodbye!')
        break

  else:
     print('The selected option is incorrect.')
        
      

  