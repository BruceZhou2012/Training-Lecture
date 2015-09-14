#coding:utf-8
__author__ = 'gubaoer'

def foo():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


##range() 没有遍历前是个生成器
#for i in xrange(10):
#    print i ###每次遍历在内存中创建

##延迟技术生成器

'''
for i in foo():
    print i

    '''
def gen():
    for i in range(10):
        x = yield i
        print x
G = gen()
print next(G)
print G.send(77)
print G.send(88)
print next(G)