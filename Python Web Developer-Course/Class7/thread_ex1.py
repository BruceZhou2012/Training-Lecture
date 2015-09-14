# coding:utf-8
import threading
import time

class MyThreading(threading.Thread):

    def run(self):
        print '小姐准备接客'
        super(MyThreading, self).run()

totally_list = []

def massage_room(i):
    lock.acquire()
    totally_list.append(i)
    lock.release()
    for j in range(1,4):
        print '第%s号小姐在为第%s个客人服务' % (i,j)

lock = threading.Lock()

for i in range(3):
    thead_obj = MyThreading(target=massage_room, args=(i,))
    thead_obj.start()
thead_obj.join()

print "今天的小姐都试了一遍，服务都真好!!!"
print totally_list




#thead_obj = MyThreading(target=massage_room, args=(1,))
#thead_obj.start()