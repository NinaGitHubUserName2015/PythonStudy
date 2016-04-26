#!usr/bin/env python
#_*_ coding:utf-8 _*_
import sys
retry_limit = 3
retry_count = 0
account_file = 'accounts.txt'
lock_file = 'account_lock.txt'

while retry_count < retry_limit:

	username = raw_input('\033[32;1mUsername:\033[0m')
	lock_check = file(lock_file)    #被锁名单文件

    #验证此用户名是否被锁
	for line in lock_check.readlines():
		line = line.split()
		if username == line[0]:
			sys.exit('\033[31;1mUser %s is locked!\033[0m' % username)

	password = raw_input('\033[32;1mPassword:\033[0m')

	f = file(account_file,'rb')     #记录账户名密码文件
	match_file = False

	#验证用户名密码是否正确
	for	line in f.readlines():
		user,passwd = line.strip('\n').split()
		if username == user and password == passwd:
			print 'Match!', username
			match_flag = True
			break
	f.close()
	if match_flag == False:
		print 'User unmatched!'
		retry_count += 1
	else:
		print "Welcome login!"

else:
	print 'Your account is locked!'
	f = file(lock_file,'ab')
	f.write(username)
	f.close()						