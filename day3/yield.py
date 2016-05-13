#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#一开始就在内存创建了0到9
print range(10)
#一开始并没有在内存创建0到9，只有遍历的时候，才会创建，只是一个生成器
print xrange(10)
for item in xrange(10):
    print item

def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    
re = foo()
#生成一个生成器
print re    
#只有当遍历的时候，才会执行，每次只执行一个yield，打印出来，延迟生成
for item in re:
    print item

'''    
#示例代码
#yield可以用来记录位置
#以后多线程的时候，可以使用yield当做一个线程池，什么时候用，什么时候拿一个过来
#yield可以保存函数的执行状态：想让函数执行到一半的时候，就不阻塞了，就是调用这个函数不会产生任何阻塞，不等它的结果，调用它一次，就立刻给返回一个值
#程序有阻塞，就会导致程序变慢，容易瓶颈
def Readlines():
    seek = 0
    while True:
        with open ('D:/temp.txt','r') as f:
            #根据某个字节跳到那个字节处接着往下读
            f.seek(seek)
            data = f.readline()
            if data:
                #得到所在当前位置
                seek = f.tell()
                yield data
            else:
                return
#打印出生成器            
print Readlines()
            
for item in Readlines():
    print item  
    
#示例：with的使用    
f = file('D:/temp.txt','r')
f.read()
f.close()
#使用with, 不用f close, 一旦跳出这一级，它会自动把f close
with open ('D:/temp.txt','r') as f: 
    pass
'''

#三元运算符
result = 'gt' if 1>3 else 'lt'
print result
              
#lambda表达式，匿名函数，这个函数很简单，并且不会在代码中经常被调用
def add(x,y):
    return x+y
print add(4,10)

temp = lambda x,y:x+y
print temp(4,10)

#map方法与 lambda表达式，这两个一起用的比较多，为了减少函数代码量
print [x*2 for x in range(10)]   #结果：[0,2,4,6,8,10,12,14,16,18]

print map(lambda x:x*2, range(10))    #结果：[0,2,4,6,8,10,12,14,16,18]














    