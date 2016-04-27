#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import tab

name_list = ['rose','jack','cat','nimo']

print name_list[1]

name_list.append('papi')     #添加
name_list.insert(2,'110')           #插入,(位置，值)
name_list.remove('110')
name_list.append('jack')
name_list.count('jack')      # 计算有多少个
name_list.index('jack')      #找到第一个的索引位置，索引保证数据在列表中是有序的
del name_list[3]
name_list.reverse()      #倒序
name_list.sort()         #按ASICC码排序
print ord('a')
name_list.extend('abcd')    #把 abcd 分开，添加进去

infos = [1,2,3,4,5,6,7]
name_list.extend(infos)     #列表相加
name_list += infos
print name_list[2:5]        #从2切到4，顾头不顾尾
print name_list[0:5]        #从头切到4，顾头不顾尾
print name_list[:5]        #从头切到4，顾头不顾尾
print name_list[-5:]        #从尾切到倒数5，顾头不顾尾
print name_list[-5]        #切第倒数5，顾头不顾尾
print name_list[-5:-1]        #从倒数1切到倒数5，顾头不顾尾
print name_list[name_list.index(2):name_list.index(2)+3]        #从2开始切3个，顾头不顾尾

#循环打出所有2的索引
first_pos = 0
for i in range(name_list.count(2)):
	new_list = name[first_pos:]
	next_pos = new_list.index(2)
	print "Find position:",first_pos + new_list.index(2)
	first _pos += next_pos 

pos = 0
for i in range(name_list.count(2)):
	if pos == 0:
		pos = name_list.index(2)
	else:	 
		pos = name_list.index(2,pos+1)     # 从 pos+1 位置开始找2的索引 
	print pos	

#从索引1开始，隔两个取一个
name_list[1::3]	

a = range(100)
a[::2]          #只取偶数
a[1::2]         #只取奇数