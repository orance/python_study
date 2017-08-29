for i in range(1,101):
    if i%2 == 0 and i%3 == 0 and i%5 == 0:
        print i,';'
print ';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])

def func(arg1,arg2):
    print arg1,arg2
func(3,7)
func(arg2=3,arg1=7)

def calcSum(*args):
    sum = 0
    for i in args:
        sum += i
    print sum
calcSum(1312,213,321,3123,3123)

abc = lambda a,b,c:a + b + c
print abc(1,23,4)

lst_1 = (1,2,3,45,6)
lst_2 = map(lambda x:x*2,lst_1)
print lst_2
