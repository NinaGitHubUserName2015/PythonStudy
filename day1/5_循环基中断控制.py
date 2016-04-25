#!/usr/bin/env python
#_*_ coding:utf-8 _*_

print_num = input('which loop do you want it to be printed out?')
count = 0
#python中有while...else...的用法
while count < 10000:
	if count == print_num:
		print 'There you got the number:',count
		choice = raw_input('Do you want to continue the loop?(y/n)')
		if choice == 'n':
			break
		else:
			while print_num <= count:
				print_num = input('which loop do you want it to be printed out?')
				print '已经过了，sx!'	
	else:
		print 'loop:',count		
	count += 1	
else:
	print '已经循环打印了10000次'	