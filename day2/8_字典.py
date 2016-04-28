#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#字典的详细用法及深浅copy的原理

#定义字典Dict, 默认没有排序,所有的key都是唯一的
name_info = {
	'name':'Jacky',
	'age':29,
	'job':'Engineer',
	'address':'BJ',
	'gender':'Male'
}

print name_info['name']        #查找
name_info['salary'] = 3000     #添加
name_info['job'] = 'IT'        #update
name_info.pop('job')        #remove
name_info.popitem()        #随机删除

#loop Dict key,i循环指向的是key
for i in name_info:
	print i

#loop Dict, 效率高
for i in name_info:
	print i, name_info[i]	

#loop Dict, 效率低
for k,v in name_info.items():
	print k, v

name_info.get('name')      #跟name_info['name']的区别在于，name_info['name']没有值会报错，name_info.get('name')不会
name_info.has_key('name')    #判断是否有这个key
name_info.keys()
name_info.values()
name_info.iteritems()       #生成器
name_info.setdefault('stuID',1123)     #如果里面有值，就返回这个值；如果不存在这个key,就加上，并赋予默认值

#合并
a = {
	'name':'Rose',
	'comment':'add'
}
name_info.update(a)

info1 = name_info     #两个指向同一个内存指针，别名，不是克隆，软链接
info2 = name_info.copy()      #另一个拷贝，浅复制，只复制第一层

#info2不会跟着name_info变化
name_info['ex_list'] = ['Coral','Emili']
print info2
print name_info

#info2跟着name_info变化，改变的是第二层，由于浅复制，所以info2跟着变了
name_info['ex_list'].append('Elena')      #给这个key加一个value
print info2
print name_info 

#深copy
import copy
info3 = copy.copy(name_info)    #浅copy             
info4 = copy.deepcopy(name_info)    #深copy

#深copy，改变第二层，info4跟着一起变
name_info['ex_list'][2] = 'Xiaohua'
print info4
print name_info            