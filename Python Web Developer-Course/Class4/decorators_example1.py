#coding:utf-8
__author__ = 'gubaoer'

'''
####
####带有返回值的装饰器
def Login(fun):

    def warpper():
        print 'Login Success'
        x = fun()
        return x
    return warpper

@Login
def func1():
    print 'fun1'
    return 'Failed'

d = func1()
print d
'''

'''
func1 =         def warpper(name):
                    print 'Login Success'
                    x = func1(name)
                    return x
'''

'''
无参数的装饰器
def Login(sdsd):
        def warpper():
                print 'Login Success'
                sdsd()
                print 'hello'
        return warpper

@Login  ###装饰器语法糖
def func1():
    print 'fun1'

func1

'''





'''
带参数的装饰器
def Login(sdsd):
        def warpper(name):
                print 'Login Success'
                sdsd(name)
                print 'hello'
        return warpper

@Login  ###装饰器语法糖
def func1(name):
    print 'fun1' + ','+ name

func1('gubaoer')
'''
'''
func1 =         def warpper(name):
                    print 'Login Success'
                    func1(name)
                return warpper()


'''





'''

def func5():
    print 'func5()'

def func6():
    print 'func6()'

def func7():
    print 'func7()'

def func8():
    print 'func8()'

def func9():
    print 'func9()'

def func10():
    print 'func10()'
'''


name = 'junjie'

split = name.split('n')