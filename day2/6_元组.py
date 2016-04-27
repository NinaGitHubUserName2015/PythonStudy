#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#元组 tuple，就是常量数组,只读，不可修改，只有2个方法
a = (1,2,3,4,2,4,5,6,2)
a.count(2)
a.index(4)

print type(a)
#列表和元组可以互相转换
a = list(a)     #转为列表
print type(a)
a = tuple(a)     #转为元组
print type(a)
