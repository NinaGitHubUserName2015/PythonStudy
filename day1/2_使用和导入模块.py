#！/usr/bin/env python

#import是导入整个模块
import os
import commands
import tab
import sys
#只导入这个模块中的一个方法
from sys import argv
import multiprocessing as mp
#下面这个不建议用
from sys import *

os.system('df')
l = os.system('pwd')
print l
os.popen('pwd')
a = os.popen('pwd').read()

res = commands.getstatusoutput('pwd')
print res

#打印执行脚本后面跟的所有参数
print sys.argv
#打印出执行脚本后面跟的第2个参数
print sys.argv[2]
