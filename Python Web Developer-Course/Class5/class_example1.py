#coding:utf-8
__author__ = 'gubaoer'

## 字段： 比如 name = value


class Person(object):    ## 定义一个类

    common = '都用两条腿走路'   ## 静态字段,也称类字段

    @staticmethod              ### 静态方法  鸡肋~~~
    def talk():
        print '都说人话'

    def __init__(self,name):    ### 构造函数，对象初始化       pe8
        self.Name = name     ## 动态字段
        self.__neiku = '穿红色内裤'     ##私有字段
        self.love = '谈恋爱'

    #def __neiku(self):
     #   print '穿红色内裤'

    def neiku(self):
        print self.__neiku     ####访问一个私有方法

    def getname(self):  ##  对象方法, 也称为动态方法
        print 'My name is %s' %(self.Name)

    @property           ###只读属性
    def love(self):
        print self.__love

    @love.setter       ### 只写属性
    def love(self,value):
        self.__love = value




junjie = Person('junjie')
chunhong = Person('chunhong')
junjie.getname()
print junjie.neiku()
print chunhong.love
chunhong.love = '快结婚了'

print chunhong.love

#print Person.common
#print junjie.common
#Person.talk()
#junjie.talk()


#qingwen = Person('zhangqingwen')

#print Person.getname()
'''
qingwen = Person()
junjie = Person()
print qingwen
qingwen.getname('qingwen')
junjie.getname('junjie')

chunhong = Person()
chunhong.getname('xuchunhong')
'''





