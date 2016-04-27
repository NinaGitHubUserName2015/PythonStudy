#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import sys,os

if len(sys.argv) <=1:
	print "usage:./file_replace.py old_text new_text filename"
old_text,new_text = sys.argv[1],sys.argv[2]

file_name = sys.argv[3]

#如果有 --bak 参数，创建备份文件
# if '--bak' in sys.argv:
# 	bak_file = '%s.bak' % file_name
# else:
# 	bak_file = None

#替换文本
f = file(file_name,'rb')
new_file = file('.%s.bak' % file_name,'wb')  #最前面那个.代表以隐藏模式打开
for line in f.xreadlines():
	#替换文字，写入文件
	new_file.write(line.replace(old_text,new_text))
f.close()
new_file.close()		

if '--bak' in sys.argv:
	os.rename(file_name,'%s.bak' %file_name) #unchanged
	os.rename('.%s.bak' %file_name, file_name) #changed
else:
	os.rename('.%s.bak' %file_name, file_name)  #replace old file	