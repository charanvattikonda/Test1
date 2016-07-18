import random
min = 0
max = 10
a = random.randint(min, max)
while True:
    b = int(input('guess the number'))
    if b < a:
        print('answer is little higher')
    elif b > a:
        print('answer is little smaller')
    elif b == a:
        print('PERFECT BITCH!')
        print('Goodbye')
        break


