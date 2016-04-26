#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tab     #加tab补全

#以只读模式打开文件
f = file('hello.txt','r')
line = f.readline()      #读一行
print line

#以只写模式打开
f = file('hello.txt','w')
f.write('new line')        #覆盖原来内容

#以追加模式打开
f = file('hello.txt','a')
f.write('second line')        #在原来内容后面追加,没有换行
f.write('\nthird line')       #换行
f.flush()

f.close