my = ['Amir', 'Reza', 'maryam', 'omid']
my2 = ['omid', 'Amir', 'Ali', 'parsa']
b = []
for x in my:
    for y in my2:
        if y == x:
            b.append(x)
            my.remove(x)
            my2.remove(x)
print(b)
print(my)
print(my2)