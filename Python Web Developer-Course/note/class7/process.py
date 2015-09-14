from multiprocessing import  Process
import time
from multiprocessing import Process, Lock

# li=[]
def sayhi(lock,name,n):
    time.sleep(2)
    lock.acquire()

