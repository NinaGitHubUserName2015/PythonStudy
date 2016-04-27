#!/usr/bin/env python
#_*_ coding:utf-8 _*_

s = "What's your Company's Name?"
s += 'NIMO'
s.find(substring,[start[,end]])     #可指范围查找子串，返回索引值，否则返回1
s.rfind(substring,[start[,end]])     #反向查找
s.index(substring,[start[,end]])     #同find,只是找不到产生ValueError异常
s.rindex(substring,[start[,end]])     #反向查找
s.count(substring,[start[,end]])     #返回找到子串的个数

s.capitalize()     #首字母大写
s.lower()          #转小写
s.upper()          #转大写
s.swapcase()       #大小写互换

l = s.split(str,'')    #将string转list, 以空格切分
s.join(list,'')    #将list转string,以空格连接
'|'.join(list)     #将list转string,以'|'连接

#处理字符串的内置函数
len(str)      #串长度
cmp("my friend",str)    #字符串比较，第一个大，返回1,等于返回0，第一个小返回-1
max('abcxyz')           #寻找字符串中最大的字符
min('abcxyz')           #寻找字符串中最小的字符
