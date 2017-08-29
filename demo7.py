##  read and write
f = file('11111.txt')
data = f.readlines()
print data
ci = raw_input()
e = file('2222.txt','w')
a = ''
b = a.join(data)
print b
e.writelines(data)
e.close()
f.close()
