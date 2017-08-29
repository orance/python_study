# _*_ coding:utf-8 _*_
L1 = ['Hello','World',18,'Apple',None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print (L2)
# Fibonacci  Python3
def fib(max):
    n,a,b = 0,1,1
    while n<max:
        print (b)
        a,b = b, a+b
        n = n+1
    return 'done'
fib(6)
# triangles
def triangles():
    L = [1]
    n = 1
    yield L
    while True:
        n = n+1
        L1 = [1]
        for i in range(1,n-1):
            L1.append(L[i-1]+L[i])
        L1.append(1)
        L = L1
        yield L1
a = 0
for t in triangles():
    print(t)
    a = a+1
    if a == 10:
        break
