#!/usr/bin/env python
#_*_ coding:utf-8 _*_
'''
两种加密方式，推荐使用第二种，第一种即将过期，MD5是不能反解的，黑客撞库
'''
import md5
hash = md5.new()
hash.update('admin')
print hash.hexdigest()

import hashlib
hash = hashlib.md5()   #生成一个对象
hash.update('admin')     #使用admin当做一个秘钥，去通过md5加密，加密之后是一个16进制的东西
print hash.hexdigest()
print hash.digest()       #和上一行的区别是，长度不同
