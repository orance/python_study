# yield返回的是一个迭代器，是一个生成规则，不是具体的值。
l = [i for i in range(0,15)]    #生成列表
print(l)
m = (i for i in range(0,15))    #生成迭代器
print(m)
for g in m:                 #for循环遍历迭代器
    print(g,end=',')         #打印迭代器的内容，end是print的函数，代表用什么结尾，默认是\n换行
