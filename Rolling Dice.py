#author-charan
import random
min = 1
max = 6
while True:
    print('please select the option')
    option = int(input("1)Roll 2)Quit"))
    if option == 1:
        print('rolling...')
        print random.randint(min, max)
    elif option == 2:
        print('Thank You')
        break
    else:
        print('please select from the options')

