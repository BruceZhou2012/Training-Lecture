__author__ = 'gubaoer'



def gensquares(N):
    for i in range(N):
        yield i ** 2

x = gensquares(4)

#print next(x)
#print next(x)



def gen():
    for i in range(10):
        x = yield i
        print x
G = gen()
'''
print next(G)
print G.send(77)
print G.send(88)
print next(G)
'''


def gen():
    for x in xrange(4):
        tmp = yield x
        if tmp == 'hello':
            print 'world'
        else:
            print str(tmp)

g=gen()
print g   #<generator object gen at 0x02801760>
print g.next()
print g.send('hello')
print g.next()

print [x ** 2 for x in range(4)]

print (x ** 2 for x in range(4))