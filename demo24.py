# yield返回的是一个迭代器，是一个生成规则，每次返回的是当前这次计算的值，不是整个list。
#返回的list是动态计算的，每次调用都是一个个的调用，不用一次性存储完整的list内容在内存，可以节省内存。
l = [i for i in range(0,15)]    #生成列表
print(l)
m = (i for i in range(0,15))    #生成迭代器
print(m)
for g in m:                 #for循环遍历迭代器
    print(g,end=',')         #打印迭代器的内容，end是print的函数，代表用什么结尾，默认是\n换行
