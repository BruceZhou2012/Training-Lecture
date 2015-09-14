#coding:utf-8
__author__ = 'gubaoer'


class Person(object):
    def __init__(self,name,job = None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay = int(self.pay * (1+percent))

    def __str__(self):
        return '[Person:%s,%s]' %(self.name,self.pay)


class Manager(object):   ##  Manager不是继承而是 作为委托嵌入进 Person类

        def __init__(self,name,pay):
            self.person = Person(name,'mgr',pay)

        def giveRaise(self,percent,bonus=.10):
            self.person.giveRaise(percent + bonus)
        def __getattr__(self, attr):
            return getattr(self.person,attr)
        def __str__(self):
            return str(self.person)





bob = Person('Bob Smith')
sue = Person('sue jones',job='dev',pay = 1000000)
print bob.name,bob.pay
print sue.name,sue.pay
print bob.lastname(),sue.lastname()
sue.giveRaise(.10)
print sue.pay
print(sue)

tom = Manager('Tom Jones',50000)
tom.giveRaise(.10)
print tom.lastname()
print tom.job


for i in tom,sue,bob:   ## 实例对象可以迭代；多态： python根据所传递的对象类型，将会自动运行相应的版本
    print i.pay

'''
实例创建  ---填充实例属性
行为方法  --- 在类方法中封装逻辑
运算符重载 --- 为打印这样的内置操作提供行为
定制行为---- 重新定义子类中的方法以使其特殊化
定制构造函数----为超类步骤添加初始化逻辑

'''
