# _*_ coding:utf-8 _*_
#保存最后N个元素
#创建固定长度的队列，depue(maxlen=X),当有新的记录加入队列已满的时候，会移除最老的那条记录

#输出匹配的文件行

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            print(prevlines)
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
