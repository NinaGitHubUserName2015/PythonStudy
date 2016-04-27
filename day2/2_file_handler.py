#!/usr/bin/env python
#_*_ coding:utf-8 _*_

f = file('hello.txt')      # 默认的打开方式是r
f = open('hello.txt','r+')      #open 和 file两种打开方式没有区别

for i in f.readlines():
	print i
	print i.strip('\n')     #表示去掉换行符，没有参数 可以去掉换行符，空格，制表符tab
	print i.strip().split(':')[0]          # 分开,成为一个列表，取列表值

f.name
f.closed
f.isatty()  #文件是否是一个终端
f.next()   #迭代使用，跟readline类似
f.read()   #以字符串形式读出所有行
f.readlines()     #以列表形式读出所有行          	
f.seek(0)       #主要用来跳到文件开始，跳到文件某个位置,可以用来处理增量日志，读取最新的一部分
f.tell()        #打出当前在文件的位置
f.truncate(100)    #从文件开头截断到第100个位置，跟当前所在位置无关

#写多行
a = range(10)       #从0到10的数字列表
a = [str(i) for i in a]    #转化为字符串列表
a = [str(i)+'\n' for i in a]   #加上换行符 
f.writelines(a)

for line in f.xreadlines():     #逐行读，读取大文件，读一行打印一行,实际上是有一个迭代器
	print line 

f.close()     
