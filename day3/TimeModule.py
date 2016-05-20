#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import time
'''
有博客地址资料
1.时间戳   1970年1月1日之后的秒
2.元组 包含了：年、日、星期等...time.struct_time
3.格式化的字符串   2014-11-11 11:11
'''

#时间戳
print time.time()
#元组
print time.gmtime()
#字符串格式化时间
print time.strftime('%Y-%m-%d %H:%M:%S')

#时间转换(字符串转元组)
print time.strptime('2011-12-12','%Y-%m-%d')
#元组
print time.localtime()
#元组转时间戳
print time.mktime(time.localtime())