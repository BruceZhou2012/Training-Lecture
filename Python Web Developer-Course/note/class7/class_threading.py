# coding:utf-8
import threading
import time


'''
def Func(i):
    print '==>',i
    time.sleep(1)
    for item in range(10):
        print item

t = threading.Thread(target=Func, args=(1,))
t.start()
t.join()    # 线程之间串行

t2 = threading.Thread(target=Func, args=(2,))
t2.start()
t2.join()    # 线程之间串行 ,join有timeout时间

print 'over'
'''

'''   可用断点
def Func(i):
    print i

t1 = threading.Thread(target=Func,args=(1,))
t1.start()
'''
dd=[]
sb = 1
def Func(i):
    lock.acquire()
    global sb
    sb += 1
    print sb
    lock.release()
    time.sleep(1)

    #for item in range(20):
    #    print item
    #sb.append(i)


class Mythread(threading.Thread):

    def run(self):
        #print 'alex------>s'
        threading.Thread.run(self)
lock = threading.RLock()

#t1 = Mythread(target=Func,args=(1,))
#t1.start()
#t2 = Mythread(target=Func,args=(2,))
#t2.start()
#t3 = Mythread(target=Func,args=(3,))
#t3.start()


for  i in range(500):
    t3 = Mythread(target=Func,args=(i,))
    t3.start()

#print sb
## 多线程共享变量，容易产生并发错乱,加锁的目的就是不允许中断，原子性