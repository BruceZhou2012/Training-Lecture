# coding:utf-8
# 生产者与消费者模型
# 优点：实现异步，解决阻塞
# 优点： 松耦合、高内聚

import  threading
from Queue import Queue
import time

queue = Queue()

def Create(i):
    while True:
        if queue.qsize() < 100:
            print i, '生产包子'
            queue.put(str(i) + '包子')  # 队列 ，先进先出，保证线程安全
        else:
            time.sleep(5)

def Producer():
    for i in range(10):
        t = threading.Thread(target=Create, args=(i, ))
        t.start()

def cosumer():
    while True:
        baozi = queue.get()
        print baozi
        print queue.qsize()
        time.sleep(2)

Producer()
cosumer()





