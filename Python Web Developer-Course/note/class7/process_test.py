#coding: utf-8
from multiprocessing import Process, Manager
import time

q_list = Manager().list()
lock = Manager().Lock()
queue = Manager().Queue()

def strip_girl(num, q_list, lock,queue):
    q_list.append(num)
    for i in range(10):
        print "第%s位妓女在接第%s个嫖客" %(num, i)
    queue.put(num)


for i in range(3):
    process_obj = Process(target=strip_girl,args=(i, q_list, lock, queue))
    process_obj.start()
    if queue.get() == 1:
        process_obj.terminate()
        process_obj.join()
        break

print q_list