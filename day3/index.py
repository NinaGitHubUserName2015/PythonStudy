#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
这是本文件描述
'''
from file import demo

name = 'Nina'
action = 'doubi'

print name,action
demo.Fool()
print 'index',__name__

#判断本程序是不是主程序
if __name__=='__main__':
    print 'Hello,Joy'
else:
    print '滚之'    

#本文件路径    
print __file__
#本文件描述
print __doc__    

