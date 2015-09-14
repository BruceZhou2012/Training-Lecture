#coding:utf-8
import threading
import time

def SB(arg):
    print 'I am' ,arg
    time.sleep(10)
    print arg

def numcount(arg):
    time.sleep(3)
    print arg

'''
t1 = threading.Thread(target=SB,args=('zhuwen',))
t1.start()

t2 = threading.Thread(target=SB,args=('gubaoer',))
t2.start()

t3 = threading.Thread(target=SB,args=('lisi',))
t3.start()
'''
for i in range(10):
    t4=threading.Thread(target=numcount,args=(i,))
    t4.setDaemon(True)
    t4.start()
    print '----end------'
    #print t4.isAlive()


# note:  其实并不是真的并行，之所以有这种错觉其实是由于cpu的时间片，
# 时间片：运行一部分 之后又运行下一部分
# start之后并不是立即执行，而是通过运行时间片
# 守护线程,当父线程执行完，不管子线程有没有结束，都会断开