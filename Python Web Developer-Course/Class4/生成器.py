#coding:utf-8
'''
print range(10)
print xrange(10)

for i in range(10000000000000000000000000000000000000000000000000000000000000000000000000000):
    print i  ##1 * 10000000000000000000000000000000000000000000000000000000000000000000000000000 倍
print 'start --->'

for x in xrange(10000000000000000000000000000000000000000000000000000000000000000000000000000):  # 生成器,  当迭代生成器的时候，它才在内存中一个一个的创建
    print x

print type(range(10))

print type(xrange(10))
'''

'''
for i in xrange(5):
    print i
    '''
'''
def fun1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for i in fun1():
    print i
    '''
'''
def fun2(N):
    for i in range(N):
        yield  i * 2

    s = []
    for i in range(N):
        s.append(i * 2)
    return s


print fun2(9)
cc = fun2(3)
print cc.next()
print cc.next()
print cc.next()
print cc.next()
'''
'''
list_1 = [1,2,3,4,5]
#for i in list_1:
#    print i
print type(iter(list_1))
cc = iter(list_1)
print cc.next()
print cc.next()
print cc.next()
print cc.next()
print cc.next()
print cc.next()
'''

'''
def gen(N):
    for i  in range(N):
        x = yield i
        if x == 'chunhong':
            print 'beautiful'
        #print x

x = gen(4)
print x

print x.next()
print x.next()
print x.send('chunhong')  ### include next.()
print x.next()
'''
Test_list = [-3,-2,-1,0,1,2,3,4,5]

#c = [i for i in Test_list if i > 1]
#print c
c = (i for i in Test_list if i > 1)
print type(c)

for i in c:
    print i