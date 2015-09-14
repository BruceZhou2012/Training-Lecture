#coding:utf8

#1.
#def sayhi():
#    print "hello,you is bitch"

#sayhi()
#sayhi()



##########################
#2.
'''
def deco(func):
    print "before sayi() called"
    func()
    print "after sayi() called"
    return func


def sayhi():
    print "hello,you is bitch"

sayhi = deco(sayhi)
sayhi()
sayhi()
'''

##############################
#3.
'''
def deco(func):
    print "before sayi() called"
    func()
    print "after sayi() called"
    return func

@deco
def sayhi():
    print "hello,you is bitch"

sayhi()
'''


##############################
#4.
'''
def deco(func):

    def _deco():
        print "before sayi() called"
        func()
        print "after sayi() called"
    return _deco

@deco
def sayhi():
    print "hello,you is bitch"

sayhi()
'''

##############################
#4.
'''
def deco(func):

    def _deco():
        print "before sayi() called"
        func()
        print "after sayi() called"
    return _deco

@deco
def sayhi():
    print "hello,you is bitch"

sayhi()
'''


##############################
#5.

def deco(func):

    def _deco(name):
        print "Success! you is logging."
        func(name)
    return _deco

@deco
def sayhi(name):
    print "hello,'%s',you is bitch" % name

sayhi('chunhong')
