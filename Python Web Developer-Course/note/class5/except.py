#coding:utf-8

__author__ = 'gubaoer'



'''


多种错误
try:

    pass



except (错误1，错误2),e:
其中e是程序真正的错误，用来记录日志


except 。。。。
可以分开
except 。。。


except  Exception,e (囊获所有的错误)



try ..... except....else



finally: 无论异常与否，都会执行


try的注意事项，一旦捕捉到tye代码块中的错误，那之后代码不会运行


'''




#自定义异常


class MyException(Exception):

    def __init__(self,msg):
        self.error = msg

    def __str__(self,*args,**kwargs):
        return self.error

#obj = MyException('错误')
#print obj

dd = 0

if dd == 0:
    try:
        raise MyException('错误')
    except MyException,e:
        print e