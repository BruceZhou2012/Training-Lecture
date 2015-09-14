x = 88
'''
def func(Y):
    global x
    x = 99


print func()
print x

def f(x):
    y = 1
    x =3
    print 'x=',x
    return x

x = 1
y = 2
z = f(x)
print 'z=',z
print 'x=',x
print 'y=',y

'''

def func():
    def func2():
        print "hello,myfum2"
    func2()
    print "hello myfun1"
d = func()

'''
def fun33(i):

    print i
    return fun33(i+4)

fun33(4)
'''

'''
def factorial(n):
    print n
    if n ==1:
        return 1
    else:
        return n * factorial(n-1)
print factorial(6)

'''

f = 'sdsds'

print isinstance(f,list)

'''
def sumtree(L):
    print L
    tot = 0
    for x in L:
        if not isinstance(x,list):
            print 'not isinstance'
            print x
            tot += x
        else:
            print 'Is isinstance'
            print x
            tot += sumtree(x)
    return tot

L = [1,[2,[3,4],5],6,[7,8]]
print sumtree(L)
'''

'''
for i in [1,[2,[3,4],5],6,[7,8]]:
    print i
'''
for i in [2, [3, 4], 5]:
    print i