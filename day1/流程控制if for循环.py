#!/usr/bin/env python
#_*_ coding:utf-8 _*_

name = raw_input('Please input your name:')
#age =  raw_input('age:')
#转化为整数
#age =  int(raw_input('age:'))
#input和raw_input的区别
#全局变量
real_age = 29
job = raw_input('job:')
salary = raw_input('salary:')

for i in range(10):
	#下面这句每次循环，都会生成一个变量，也是全局变量
	#real_age = 30
	age =  input('age:')	
	if age>29:
		msg = 'You are too fucking old!'
		print 'think smaller!'
	elif age<29:
		msg = 'You still have a few years to up.'
		print 'think bigger!'
	else:
		msg = 'You are still quite young.'
		#加上颜色高亮显示，是shell的写法,32是绿色字体，42是绿色底
		print '\033[42;1mGOOD! 10 RMB!\033[0m'
		break
	print 'You still got %s shots' % (9-i)		

#格式化输出
print '''
Personal information of %s:
  		  Name: %s
  		  Age ：%d
  		  Job : %s
  	   	Salary : %s
  	  	Message ：%s
-----------------------------------
''' % (name,name,age,job,salary,msg)


