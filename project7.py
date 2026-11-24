x = int(input('enter your day: '))
y = int(input('enter your month: '))
z = int(input('enter your year: '))

def shamsi(x,y):
    if y >= 10 and x > 10:
        p = z + 622
    else:
        p = z + 621
    return p

def Miladi(x,y):
    if x > 21 and y >= 3:
        q = z - 622
    else:
        q = z - 621
    return q

if z > 1600:
    s = Miladi(x,y)
    print(f'Your date of birth, in the Solar calendar, corresponds to {y} {x}, {s}.')
else:
    v = shamsi(x,y)
    print(f'Your date of birth, in the Gregorian calendar, corresponds to {y} {x}, {v}.')

    