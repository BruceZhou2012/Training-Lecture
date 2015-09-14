#coding:utf8
__author__ = 'gubaoer'

dd = open('myfile.txt')
#print type(dd)

myfile = open('myfile.txt','w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.write('see you again')
myfile.write('see you again,too')
myfile.writelines(('c','h'))
myfile.writelines(['1','2','3','4','5'])
#myfile.writelines([2,3])
myfile.close()


myfile = open('myfile.txt')
#print myfile.read(5)
myfile.close()

myfile = open('myfile.txt')
#print myfile.readline(16)

myfile.close()


myfile = open('myfile.txt')
#print myfile.readlines()
myfile.close()

'''
myfile = open('myfile.txt','r+')
print myfile.readline()
print myfile.tell()
myfile.seek(myfile.tell())
myfile.write('chunhong\n')
myfile.close()
'''
'''
with open('myfile.txt','r+') as chunhong:
     print chunhong.readline()
     print chunhong.tell()
     chunhong.seek(chunhong.tell())
     chunhong.write('chunhong\n')

myfile = open('myfile.txt')
for i in myfile.read():
    print i
myfile.close()
'''
'''
myfile = open('myfile.txt')
for i in myfile:
    print i
myfile.close()
'''
'''
ip_set3 = [ i for i in range(1,3)]
ip_set4 = [ i for i in range(1,8)]
file_list = [ "192.168.%s.%s\n" %(i,j) for i in ip_set3 for j in ip_set4  ]
print file_list

with open('file_test.txt','w') as writer:
    writer.writelines(file_list)
for i in open('file_test.txt','r'):
    print i
'''

'''
D = {'a':1,'b':2}
F = open('detafile.pkl','wb')
import pickle
pickle.dump(D,F)
F.close()

F = open('detafile.pkl','rb')
E=pickle.load(F)
print E
'''
'''
myfile = open('myfile.txt')
#print myfile.readline()
#print myfile.readline()
print myfile.next()
print myfile.next()
print myfile.next()
print myfile.next()   ## next(myfile)
myfile.close()
'''




def time(x,y,c):
    return x , y ,c


#print time(x= 1,y=2,3)
'''
def f(x):
    def g():
        x = 'abc'
        print 'x =',x
    def h():
        z = x
        print 'z =',z
    x = x +1
    print 'x=',x
    h()
    g()
    print 'x = ',x
    return g
x = 3
z = f(x)

print 'x =',x
print 'z =',z
print z()

'''

'''
def f(a,*pargs,**args):
    print (a,pargs,args)

print f(1,2,3,x=1,y=2)


def func(a,b,c,d):
    print a,b,c,d

args = {'a':1,'b':2,'c':3}
args['d'] = 4
func(**args)
'''


def maker(N):
    def action(x):
        return x**N
    return action

f=maker(2)
print f
print f(3)
print f(4)




