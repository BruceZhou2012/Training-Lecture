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

    def __str__(self):        ##运算重载符    ,解决print(bob)
        return '[Person:%s,%s]' %(self.name,self.pay)

class Manager(Person): ### 子类Manager继承父类Person

        def __init__(self,name,pay):  ##自定义Manager子类构造函数
            super(Manager,self).__init__(name,'mgr',pay)   ##继承父类的构造函数，并修改其功能；manager 不需要填写job信息了
        #def giveRaise(self,percent,bonus = .10):       ##重写父类方法，尽管没有问题，但会不够灵活，所以这是不推荐的写法
        #    self.pay = int(self.pay * (1 + percent + bonus))
        def giveRaise(self,percent,bonus=.10):
            Person.giveRaise(self,percent + bonus )   ##在原有的方法上扩展
        def someThingElse(self):
            pass



'''
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



实例创建  ---填充实例属性
行为方法  --- 在类方法中封装逻辑
运算符重载 --- 为打印这样的内置操作提供行为
定制行为---- 重新定义子类中的方法以使其特殊化
定制构造函数----为超类步骤添加初始化逻辑

'''
