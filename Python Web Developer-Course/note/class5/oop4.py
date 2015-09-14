#coding:utf-8
__author__ = 'gubaoer'

##单继承


class Father(object):

    def __init__(self):
        self.Fname = 'ffff'

    def Func(self):
        print 'father.Fcun'

    def Bad(self):
        print 'father.抽烟喝酒烫头'

class Son(Father):
    def __init__(self):
        super(Son,self).__init__()     ###加载父类init
        self.Sname = 'ssss'

    def Bar(self):
        print 'son.bar'

    #def Bad(self): ##重写

     #   print 'son bad'

    def Bad(self):  ##重写+继承
        Father.Bad(self)
        print 'son.赌博'


d = Son()

d.Bad()
print d.Fname

#######
'''
新式类 &  经典类

__slot__ 只能调用类中的某个方法


新式类在经典类的基础上，新增了很多特性
还新加了 多重继承

经典类   深度优先算法
新式类 广度优先算法

'''


###多重继承





'''
class A:   ####这个例子是经典类的例子，由于使用深度优先算法，因此它永远找不到C的save方法，这是最大的bug
    def __init__(self):
        print 'this is A'

    def save(self):
        print 'save method from A'

class B(A):
    def __init__(self):
        print 'this is B'

class C(A):
    def __init__(self):
        print 'this is C'
    def save(self):
        print 'save method from C'

class D(B,C):
    def __init__(self):
        print "this is D"

c = D()
c.save()
'''

####抽象类
from abc import ABCMeta,abstractmethod
class Alert(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def Fun(self):
        pass
    # 抽象类+抽象方法=接口 ，就是规范

class Foo(Alert):
    def __init__(self):
        print '__init__'

    def Fun(self):
        print 'hahah'

Foo()
'''
第二种接口 （在python中这种实现有点困难，因为没有静态约束，但可以用抽象类的方法）


架构师定义一个  软件框架类和方法（里面什么都没有都是pass）

程序猿继承这个类来写类中的方法，不然就会报错
'''