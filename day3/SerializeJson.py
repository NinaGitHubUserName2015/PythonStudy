#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import pickle

li = ['Nina','happy',11,22,'love']
#序列化
dumpsed = pickle.dumps(li)
print dumpsed
print type(dumpsed)
#反序列化
loadsed = pickle.loads(dumpsed)
print loadsed
print type(loadsed)

#序列化后，写进文件temp.pk里
pickle.dump(li,open('D:/temp.pk','w'))
#反序列化,从文件读进内容
result = pickle.load(open('D:/temp.pk','r'))
print result

'''
除了pickle，还有json，用法是一样的，区别是：
1.pickle只能在python中使用，是python自己做的；json是所有的语言都支持的一种接口数据格式
2.pickle不单可以dump常规的数据类型，还可以序列化类和对象，基本上python中所有的数据类型都可以被序列化；
  json只能序列化常规的数据类型，就是字典、列表、集合等，因为在不同的语言里，写一个类的语法完全不一样
'''
#json序列化之后，还是肉眼可读，pickle不可读；
import json
name_dic = {'name':'Nina','age':23}
serialized_obj = json.dumps(name_dic)
print serialized_obj
print type(serialized_obj)
#json反序列化，json序列化是以unicode编码存储的，所以反序列化后，从utf-8变成unicode编码
print json.loads(serialized_obj)



