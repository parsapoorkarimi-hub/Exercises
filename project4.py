def me(d):
    b = len(d)
    if b < 8:
          print('your password must be at least 8 char')
    elif d.isnumeric():               # بررسی میکنه که تمام استرینگ عدد باشد که اگر نباشد فالس نمایش می دهد
          print("your password must have at list one letter")
    elif d.isalpha():                    #بررسی میکنه که تمام استرینگ حروف الفبا باشد که اگر نباشد فالس نمایش می دهد
         print('your password must have at least one number')
    else :
         print('yes')

while True:
    a = input('enter your password: ')
    me(a)


    



