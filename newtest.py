l = int(input('length=?'))
b = int(input('breadth=?'))
a = l*b
p = 2*(l+b)
c = ((l**2)+(b**2))**0.5
while True:
 print('1 Area 2 perimeter 3 Diagonal_length 4 quit')
 option = int(input('please select the option'))
 if option == 1:
    print('area is',a)
 elif option == 2:
    print('perimeter is',p)
 elif option == 3:
    print('Length of the diagonal is',c)
 elif option == 4:
    print('Good bye')
    break
 else:
    print('please choose correct option')