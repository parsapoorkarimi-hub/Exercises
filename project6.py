a = int(input('enter your number: '))

def my(a):
    if int(a % 2) == 0:
        print('the number is even')
    else:
        print('the number is odd')

while True:
    my(a)
    a = int(input('enter your number: '))