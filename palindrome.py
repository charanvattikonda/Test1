while True:
   a = int(input('enter the number'))
   b = str(a)
   if b[0] == b[-1]:
      print 'its a palindrome'
   elif b[0] != b[-1]:
        print 'not a palindrome'
