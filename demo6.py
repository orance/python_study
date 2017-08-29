print range(1,10)
I = range(0,10)
I[4]=1000
print I[3]
I.append(1024)
a = I[1:-3]
print a
del I[4]
for i in I:
    print i,
print
sentence = 'I, have a ,dream'
print sentence.split(',')
