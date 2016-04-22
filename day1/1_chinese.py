#_*_ coding:utf-8 _*_
name = u'中文'
print name

#转化为utf-8
a = name.encode('utf-8')

b = a.decode('utf-8')

type(a)
print a
type(b)
print b

#得到a的ASSIC
ord('a')