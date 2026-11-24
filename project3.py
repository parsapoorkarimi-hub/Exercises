a = input('enter your name: ')
c = []
a = a.lower()
a = a.replace(' ','')            #جایگزین کردن

for x in a:
        if x not in c:
         b = a.count(x)
         print(f'your name has {b} {x}')
         c.append(x)        



