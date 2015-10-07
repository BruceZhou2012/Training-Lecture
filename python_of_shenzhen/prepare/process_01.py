# coding: utf-8

import multiprocessing
import time


# totally_pay = []

def massage_root(i, Q):
    l.append(i)
    Q.put(i)
    for j in range(1, 4):
        print('第%s位技师,为第%s位客人服务' % (i, j))


manager = multiprocessing.Manager()
l = manager.list()
Q = manager.Queue()

for i in range(3):
    p = multiprocessing.Process(target=massage_root, args=(i, Q))
    p.start()
    if Q.get() == 1:
        print '警察来例行检查'
        p.terminate()
        break
p.join()
print '今天的生意真好啊!'


print l
