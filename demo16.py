import math
x = 1.2
a = math.ceil(x)
b = math.floor(x)
c = math.pow(a,b)
d = math.sqrt(c)
print (a,b,c,d)     #python3

def fangcheng(x,y,z):
    c1 = (-y + math.sqrt(math.pow(y,2) - 4*x*z))/(2*x)
    c2 = (-y - math.sqrt(math.pow(y,2) - 4*x*z))/(2*x)
    print (c1,c2)
fangcheng(1,2,-1)
