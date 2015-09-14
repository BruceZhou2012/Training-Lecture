__author__ = 'gubaoer'


'''
myfile = open('myfile.txt','w+')
myfile.writelines('dddddddddddddddddddddafdsfsfdsfsfsd\n')
myfile.writelines(['1','3','5'])
#print myfile.readlines()
myfile.close()
'''
myfile = open('myfile.txt','r')
print myfile.next()
print myfile.next()
#print myfile.next()


i = [1,2,3]
I = iter(i)
print I.next()
print I.next()
print type(I)

x = []
for i in range(10):
    if i % 2:
        x.append(i)
print x


