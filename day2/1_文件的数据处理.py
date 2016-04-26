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

#以写读模式打开,写读模式是说清空这个文件，然后再往里面写
f = file('hello.txt','w+')

# b代表二进制，在 linux 上面没有用，在 windows 上使用:
# linux上面换行是 \n , window上面换行是 \n\r;
# linux上面有一个命令是dos2unix，意思是把 windows 格式写的代码或文本文件转换成linux格式；
# b可以自动把 \n\r 转化为 \n;
# 例外：linux上面有一个包 zipfile, 可以直接通过这个包读取 zip包，这个时候必须要加上 b.

f.close