a = input('enter your name: ')

def me(a):
    count1 = 0
    count2 = 0
    for x in a:
        if x.islower():              #بررسی حروف کوچک و خروجی فالس یا ترو 
            count1 += 1
        elif x.isupper():            #بررسی حروف بزرگ و خروجی فالس یا ترو
            count2 += 1
    print(f'lower case: {count1}')
    print(f'upper case: {count2}')

while True:
    me(a)
    a = input('enter your name: ')


    
    
