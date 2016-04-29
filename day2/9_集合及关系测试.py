#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#去重复，无序
name_set = {1,2,4,5}
#有序列表
a = range(100)
#转为集合
a = set(a)

a.add(100)   #添加
a.pop()      #删除

x = {1,2,3,4}    #x = set([1,2,3,4])    报错：invalid syntax
y = {3,4,5,6}    #y = set([3,4,5,6]) 

#测试 x 和 y 之间的关系
x & y       #求交集 a.intersection(b)
x | y       #求并集 a.union(b)
x - y       #在 x 不在 y 里面的差集 a.difference(b)   
x ^ y       #求对称差集，去掉 x 和 y 都有的 a.symmetric_difference(b)
a.issubset(b)     #a 是否是 b 的子集
a.issuperset(b)   #a 是否包含 b
