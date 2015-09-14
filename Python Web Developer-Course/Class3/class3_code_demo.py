myfile = open('myfile.txt','w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.write('see you again')
myfile.write('see you again,too')
myfile.close()

myfile = open('myfile.txt','r+')
#print myfile.read()
#print myfile.tell()
#myfile.seek(0)
#print myfile.readline()
myfile.seek(5)
myfile.write('gubaoer')
#print myfile.read()
myfile.close()

myfile = open('myfile.txt','r')
print myfile.readlines()
#print myfile.readlines()
myfile.close()

myfile = open('myfile.txt','w+')
myfile.writelines('dddddddddddddddddddddafdsfsfdsfsfsd')
myfile.writelines(['1','3','5'])
#print myfile.readlines()
myfile.close()

dd = []
myfile = open('myfile.txt','r')
for i in myfile.readlines():
    print dd.append(i)
myfile.close()
print dd


ip_set3 = [ i for i in range(1,3)]
ip_set4 = [ i for i in range(1,8)]
file_list = [ "192.168.%s.%s\n" %(i,j) for i in ip_set3 for j in ip_set4  ]
print file_list

with open('file_test.txt','w') as writer:
    writer.writelines(file_list)
for i in open('file_test.txt','r'):
    print i

file_test = open('file_test2.txt')
dd_list = []
for i in file_test:
    dd_list.append(i.strip('\n'))
finally_list = sorted(dd_list)
print finally_list
'''

D = {'a':1,'b':2}
F = open('detafile.pkl','wb')
import pickle
pickle.dump(D,F)
F.close()

F = open('detafile.pkl','rb')
E = pickle.load(F)
print E

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


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot +=x
        else:
            tot += sumtree(x)
    return tot

L = [1,[2,[3,4],5],6,[7,8]]
print sumtree(L)


def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

print factorial(6)


