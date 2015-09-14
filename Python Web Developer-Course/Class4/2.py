#coding:utf-8
__author__ = 'gubaoer'


'''
def func():
    print 'persent:func1'
    def subfunc(name):
        print 'sub:func2',name
        def threefunc():
            print 'three:func3'
        return  threefunc
    return subfunc

a = func()
a_1 = a('test')
print a_1()
'''


'''
def t1():

    def t2():
        return 1

    return 87878
    '''
'''
counts=[1,2,3,4]
s=[]
for i in  counts:
   s.append(i+10)
#print s
'''
'''
d =[ i+10 for i in counts ]
print d
'''
'''
map(function,list)  ####map 语法
'''

'''
counts=[1,2,3,4]
def sum(x):
    return x + 10

x = map(sum,counts)
print x
'''
test=[-3,-2,1,2]
print filter(lambda x:x>1,test)


print reduce((lambda  x,y:x + y),[1,2,3,4,6,7,9])

#(1+2) + (3+4) + (6+7) + 9


