#Martix = [[1,2,3],[4,5,6],[7,8,9]]
#
#testlist = []
#for i in Martix:
#    print str(i[1])
#    testlist.append(str(i[1]))
#
#print testlist
#print eval('+'.join(testlist))
#print '+'.join(testlist)

##C = {'a':1,'b':2,'c':3}
##
##d = C.keys().sort()
##for i in d:
##    print i,C[i]

'''
x = [ i for i in range(1,6) ]
y = [ i for i in range(1,256) ]
print x ,y

for xx in x:
    for yy in y:
        print '192.168.%s.%s' %(xx,yy)
'''

'''
while True:
    i = raw_input('please input number:')
    if i == '4':
        print 'sorry,you is wrong'
        break
    else:
        print i
'''

cunkuan = 10000
years = 0
while cunkuan < 20000:
    years +=1
    cunkuan = cunkuan * (1 + 0.019)
    print years,cunkuan
#print years




