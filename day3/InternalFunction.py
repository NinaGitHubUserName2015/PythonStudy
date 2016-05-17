#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#内置函数
a = []
help(a)
print dir()   #以字符串形式列出当前文件所有的变量和方法名的key
print vars()   #以map形式列出当前文件所有的变量和方法名的key:value
print type(a)
import function   #当第一次导入的时候，就会执行一遍function里面的所有东西，python做了优化，再次import的时候，不会再执行一遍
reload(function)  #去掉python再次import做的优化，再执行一遍
id(a)

print abs(-9)   #绝对值
print bool(0)   #False
print bool(None)   #False
print bool('')   #False
cmp(2,3)
print divmod(9,4)  #(2,1)  被除数除以除数等于（商，余数），计算分页
print max([11,22,33,44])
print min([11,22,33,44])
print sum([11,22,33,44])
print pow(2,10)    #指数
#############################################################
len()       #长度，如果是中文，计算的是字节的长度，不是字符的长度
print all([1,2,3,0])      #False,参数是一个可迭代的,函数会遍历参数里所有的值，如果全部为true，就输出True，否则输出False
print all([1,2,3,1])      #True,参数是一个可迭代的
print any([0,0,0,0])      #False,参数是一个可迭代的,函数会遍历参数里所有的值，如果全部为false，就输出False，否则输出True
print any([1,0,0,0])      #True,参数是一个可迭代的
#############################################################
print chr(66)       #B,输出数字对应字符，ASCII码
print ord('A')      #65,与chr()对应
#############################################################
print hex(20)       #16进制
print oct(20)       #8进制
print bin(20)       #2进制
#############################################################
li = ['手表','汽车','房']
for item in li:
    print item
    
for item in enumerate(li):      #加上了序号，默认从0开始
    print item    

for item in enumerate(li,1):      #加上了序号，从1开始
    print item 
    
for item in enumerate(li,1):      #加上了序号，从1开始,可以通过索引找到具体的值
    print item[0],item[1]  
    
for k,v in enumerate(li,1):      #加上了序号，从1开始,可以通过索引找到具体的值
    print k,v
############################################################
#字符串的格式化,跟%s占位符效果是一样的
s = 'I am {0}'
print s.format('Nina')       
s = 'I am {0},{1}'
print s.format('Nina','Joy')    
############################################################
def Function(arg):
    print arg
Function('aaaa')    
apply(Function,('aaaa'))    #执行函数
###########################################################
def foo(arg):
    return arg+1
li = [1,2,3,4]
print map(foo,li)     #遍历后面的列表，执行前面的函数,返回一个新的列表list
print map(lambda arg:arg+2,li)
    
def foo2(arg):
    if arg<20:
        return True
    else:
        return False
li2 = [18,21,19,22]
print filter(foo2,li2)    #遍历后面的列表，执行前面的过滤,返回一个新的列表list,满足True    
print filter(lambda arg:arg == 2,li)

print filter(lambda x,y:x+y,[1,2,3])    #累加

x = [1,2,3]
y = [4,5,6]
z = [4,5,6]
print zip(x,y,z)
x = [1,2,3]
y = [4,5]
z = [4,5,6]
q = [5,8,9,0]
print zip(x,y,z,q)
########################################################################
a = '8*8'         #字符串
print eval(a)       #计算出8乘8，把字符串当做表达式执行
########################################################################
#反射，以字符串形式导入模块
temp = 'sys'      #要求：导入sys模块
module = __import__(temp)
print module.path
    
#使用不同的数据库服务器
sqlserver = True    #主数据服务器连接正常   
if sqlserver:
    temp = 'sqlserverhelper'     
else:
    temp = 'mysqlhelper'       #备份数据库，如果主数据服务down机了，迅速切换到备份数据服务
module = __import__(temp)
print module.count()           #调用服务器方法

#反射，以字符串形式执行函数
func = 'count'
Function = getattr(module, func)      #在module这个模块里面找到count这个函数,并返回
Function()
    
    
    
    
    
    
    
    
    
    
    
    
    
    