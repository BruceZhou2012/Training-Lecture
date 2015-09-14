# coding:utf-8

import  multiprocessing


def massage_room(i, lock, queue):
    lock.acquire()
    List.append(i)
    lock.release()
    for j in range(1,4):
        queue.put(j)
        print '第%s号小姐在为第%s个客人服务' % (i,j)

manager = multiprocessing.Manager()
List = manager.list()
lock = manager.RLock()
queue = manager.Queue()

for i in range(3):
    process_obj = multiprocessing.Process(target=massage_room, args=(i, lock, queue))
    process_obj.start()
    if queue.get() == 3:
        process_obj.terminate()
        break
    process_obj.join()


print "今天的小姐都试了一遍，服务都真好!!!"
print List