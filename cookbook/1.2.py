# _*_ coding:utf-8 _*_
# 从任意长度的可迭代对象中分解元素
#在爬虫中用于截取有用的部分信息

#去掉第一个和最后一个，取中间值的平均数,middle四个列表变量
def avg(x):
    return sum(x)/len(x)
def drop_first_lsat(grades):
    first,*middle,lsat = grades
    return avg(middle)
L = [x for x in range(24)]
s = drop_first_lsat(L)
print(s)
#对于已知部分内容，未知其他内容的情况，用*可以方便取得想要的内容
records = [
('foo',1,2),
('bar','Hello'),
('foo',1,3)
]
def do_foo(x,y):
    print('foo',x,y)
def doo_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        doo_bar(*args)

#用于特定格式的字符串的处理，比如用：或者其他特殊符号隔开的情况
line = 'nobody:*:-2:-2:dasdsadsa:/var/empty:/user/bin/false'
username,*files,home,sh = line.split(':')
print(username)
print(home)
print(sh)
print(*files)

#可以用_或者ign用来代表待丢弃的变量名
recode = ('cheng',50,123,(12,12,2017))
name,*_,(*ign,year) = recode
print(name)
print(year)
