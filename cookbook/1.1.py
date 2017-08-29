# _*_ coding:utf-8 _*_
#将序列分解为单独的变量
p = (4,5)
x,y = p
print(x)
print(y)

#只要格式一致就可以直接赋值，数量不匹配的时候会报错
data=['Hello',50,1.23,(2012,12,12)]
name,shares,price,(year,month,day) = data
print(name)
print(shares)
print(price)
print(year)
print(month)
print(day)

#任何可以迭代的对象都可以直接这样赋值，包括元组、列表、字符串等
s = 'Hello'
a,b,c,d,e = s
print(c)

#有些不想用到的值，就用一个用不到的变量名制定，但是一定要一一对应
