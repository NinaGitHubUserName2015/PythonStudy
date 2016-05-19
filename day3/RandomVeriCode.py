#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import random

print random.random()      #0到1之间随机数
print random.randint(1,5)    #[1,5]之间随机整数
print random.randrange(1,10)   #[1,10)之间随机整数

#生成包括数字和字母的6位验证码
code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(0,9)))
    else:
        temp = random.randint(65,90)
        code.append(chr(temp))
print ''.join(code)            