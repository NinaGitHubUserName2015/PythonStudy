#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#函数
#不做重复的工作，代码复用
def Chop(name):
    print name,'去砍柴'
    
Chop('Nina')
Chop('Joy')

#参数，action是可选参数，有默认值'砍柴'，有默认值我的参数要放在后面
def Func(name,where='北京',action='砍柴'):
    print name,'去',where,action
    
Func('Nina',action='玩')
Func('Joy',action='吃饭')
Func('Elena')

def login(username):
    if username == 'admin':
        return '登陆成功'
    else:
        return '登陆失败'
        
def detail(user):
    print user,'xxxxxxxxxxxxx'        
    
if __name__ == '__main__:':
    user = raw_input('请输入用户名：')
    #函数有返回值
    result = login(user)
    if result == '登陆成功':
        detail(user)
    else:
        print result
        
def show1(arg):
    for item in arg:
        #各种炫酷效果打印
        print item 

def show2(arg1,arg2,arg3):
    print arg1,arg2,arg3
    
def show3(*arg):
    for item in arg:
        #各种炫酷效果打印
        print item
        
def show4(**kargs):
    for item in kargs.items():
        #各种炫酷效果打印
        print item
               
#参数是一个列表        
show1(['Nina','Joy','Elena'])
show2('Nina','Joy','Elena')
#参数可变，不管你传多少个参数，python都自动汇总包装成一个列表参数传给函数
show3('Nina','Joy','Elena','Nina','Joy','Elena','Nina','Joy','Elena') 
#参数可变，不管你传多少个参数，python都自动汇总包装成一个字典参数传给函数
show4(name='Nina',age='14',gender='female')               
user_dict = {'k1':123,'k2':456}
#传一个字典进去，要加上**
show4(**user_dict)

