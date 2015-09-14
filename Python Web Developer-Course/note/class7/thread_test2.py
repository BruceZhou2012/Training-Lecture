# coding: utf-8
import threading


def strip_girl(num):
    print "第%s位妓女在接客" %(num)

class Mythread(threading.Thread):

    def run(self):
        print '开张'
        super(Mythread, self).run()
        #threading.Thread.run(self)


thread_obj2 = Mythread(target=strip_girl,args=(1,))
thread_obj2.start()