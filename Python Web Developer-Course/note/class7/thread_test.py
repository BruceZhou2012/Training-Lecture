# coding: utf-8
import threading
import time

dd = []

def strip_girl(num):
    lock.acquire()
    dd.append(num)
    lock.release()
    for i in range(10):
        print "第%s位妓女在接第%s个嫖客" %(num, i)


#thread_obj1 = threading.Thread(target=strip_girl,args=(1,))
#thread_obj1.start()
lock = threading.Lock()
for  i in range(5):
    thread_obj2 = threading.Thread(target=strip_girl,args=(i,))
    thread_obj2.start()

thread_obj2.join()
print dd
print '警察来了'
