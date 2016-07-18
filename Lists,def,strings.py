a = [1,2,3,4,5]
a.append(6)
a.insert(2,7)
a.extend([8,9,10])
print sorted(a),len(a),a[0]
a[0] = 4
print a[0]
print a
b = (1,2,3,4)
print b
print b[0]