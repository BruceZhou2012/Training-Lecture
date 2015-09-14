 #coding:utf-8

class Myexception(Exception):
    def __init__(self,msg):
        self.message = msg
        #print self.message

c = [1,2,3]

try:
    if 2 in c:
        raise Myexception('对不起，你的列表中有非法数字2')
except Myexception,e:
    print e.message
else:
    print 'Success'


