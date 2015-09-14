#coding:utf-8
__author__ = 'gubaoer'

##构造函数__init__

###析构函数__del__ 当python销毁对象的时候，你需要程序做些什么

class Foo(object):
    def __init__(self):
        pass

    def __del__(self):
        print '解释器要销毁我啦'   #####你很少用到，使用场景举例，假设你打开一个文件，但忘记关闭释放

    def  __call__(self):
        print 'call'


###call方法，比较变态  Python特色方法
f1 = Foo()   ###执行__init__方法

#f1()   #当你用call 可以这么用




