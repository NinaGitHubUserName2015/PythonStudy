#!/usr/bin/env python
#_*_ coding:utf-8 _*_

name = raw_input('Please input your name:')
#age =  raw_input('age:')
#转化为整数
age =  int(raw_input('age:'))
#input和raw_input的区别
age =  input('age:')
job = raw_input('job:')
salary = raw_input('salary:')

#格式化输出
print '''
Personal information of %s:
  		  Name: %s
  		  Age ：%d
  		  Job : %s
  	   Salary : %s
-----------------------------------
''' % (name,name,age,job,salary)


