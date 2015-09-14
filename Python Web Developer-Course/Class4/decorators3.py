#coding:utf-8
__author__ = 'gubaoer'


'''
#无参
def outer(fun):
    def wrapper():
        print 'Success'
        fun()
        print 'hahah'
    return wrapper



@outer
def Func1():
    print 'func1'
Func1()


Func1=
    def wrapper():
        print 'Success'
        fun()
        print 'hahah'

'''

'''
#有参
def outer(fun):
    def wrapper(arg):
        print 'Success'
        fun(arg)
        print 'hahah'
    return wrapper



@outer
def Func1(arg):
    print 'func1',arg

Func1('gubaoer')

Func1=
    def wrapper(arg):
        print 'Success'
        fun(arg)
        print 'hahah'

'''
#有返回值
def outer(fun):
    def wrapper(arg):
        print 'Success'
        result = fun(arg)
        print 'hahah'
        return result
    return wrapper

@outer
def Func1(arg):
    print 'func1',arg
    return 'gubaoer'

dd = Func1('jjjj')
print dd

'''
Func1=
    def wrapper(arg):
        print 'Success'
        result = fun(arg)
        print 'hahah'
        return result


'''


'''

@outer   ###@outer = outer(Func1)
def Func2():
    print 'func2'

@outer
def Func3():
    print 'func3'


Func1()

Func2()

Func3()
'''

