#coding:utf8
import time


'''
def foo():
    print 'in foo()'
foo()



def foo():
    start = time.clock()
    print 'in foo()'
    end = time.clock()
    print 'used:',end - start

foo()



def foo():
    print 'in foo()'

def timeit(func):
    start = time.clock()
    func()
    end = time.clock()
    print 'used:',end - start
timeit(foo)
'''

'''
def login_requeire(func):

    print 'Ypu have logged in!'
    return func()

@login_requeire
def sayhi():
    print 'hello,blueshit!'

#sayhi = login_requeire(sayhi)
print sayhi

'''

def login_requeire(func):       #你只能这么写
    print 'Ypu have logged in!'
    #return func()
    def wrapper(arg):
        print 'arg--level'
        return func(arg)
    return wrapper

@login_requeire
def sayhi(name):
    print '%s:hello,blueshit!' % name

#sayhi = login_requeire(sayhi)
print sayhi('gubaoer')

#一千个函数，如果突然要为这个函数添加一个认证方法