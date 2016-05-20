#!/usr/bin/env python
#_*_ coding:utf-8 _*_

#reg模块，正则表达式
import re

result1 = re.match('\d+','shi134mb24nm6479vv')   #从给定的字符串起始处去匹配，找到即返回，返回值是一个对象
print 'result1_obj:',result1
#如果找到对象，打印找到的内容
if result1:
    print 'result1:',result1.group()

result2 = re.search('\d+','shi134mb24nm6479vv')    #从给定的字符串整个去匹配，找到一个即返回，返回值是一个对象
print 'result2_obj:',result2
if result2:
    print 'result2:',result2.group()
    
result3 = re.findall('\d+','shi134mb24nm6479vv')   #找到所有的，返回值是一个列表
print 'result3:',result3

#把定义的表达式编译了一下,返回的对象跟re有一样的函数
#好处：定义一个表达式，编译之后，可以在n条字符串里面匹配数据，重复使用，速度快
#re本质上也是先进行compile，再进行匹配操作
com = re.compile('\d+')
print type(com)
result4 = com.findall('shi134mb24nm6479vv')
print 'result4:',result4   

'''
\d 代表数字；
\w 代表 下划线，字母，数字，还有中横杠；
\t 代表制表符；
. 代表除了回车以外的所有字符
* 大于等于0
+ 大于等于1
？ 0或1
{m} m次
{m,n}  m到n次
'''
#分组，组要用（）括起来
#分组是只获取组里的东西
result5 = re.search('(\d+)\w*(\d+)','shi134mb24nm6479vv')    #从给定的字符串整个去匹配，找到一个即返回，返回值是一个对象
print 'result5_obj:',result5
if result5:
    print 'result5_group:',result5.group()
    print 'result5_groups:',result5.groups()
    
#匹配一个ip地址
ip = 'udjkjg43.13.45.jjasklf45.69.6bcjs;.192.168.13.45hjhgf67'
print 'ip:',re.findall('(?:\d{1,3}\.){3}\d{1,3}',ip)    
    