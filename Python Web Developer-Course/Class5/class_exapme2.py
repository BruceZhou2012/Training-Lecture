#coding:utf-8
__author__ = 'gubaoer'

'''
class A:

    def __init__(self):
        self.__sex = 'man'
    def name (self):
        print 'name 1'

    @property
    def sex(self):
        print  self.__sex
    @sex.setter
    def sex(self,value):
        self.__sex = value
a = A()
print a.name()
a.sex = 'women'
print a.sex
'''

'''
a.py
def name(name):
    print 'hello %s ' %(name)

b.py
def name(name):
    print  'hello %s ' %(name)

函数----- 自省（反射）   100% 高度替换掉 面向对象

'''
'''
class A(object):
    def name(self,name):
        print 'hello %s ' %(name)

s = A()
'''


class  Foo(object):
    def __init__(self):
        #self.Name = name
        print '俊杰杀了我'

    #def __del__(self):
     #   print '我要自杀了'

    def __call__(self, *args, **kwargs):
        print 'hello'




ff = Foo()
print ff()

