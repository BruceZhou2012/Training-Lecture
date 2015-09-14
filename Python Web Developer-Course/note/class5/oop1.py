#coding:utf-8

##类和对象，静态字段
__author__ = 'gubaoer'


class Province(object):
    memo = '23 number'     ##类变量

    def __init__(self,name,capital,leader):
        self.Name = name          ### self.xxxx属于对象变量
        self.Capital = capital
        self.Leader = leader

    def sports_meet(self):        #### 动态方法
        print self.Name + '正在开运动会'


    @staticmethod            ###静态方法，属于类
    def Foo():
        print '省要带头反腐'

    @property                ### 动态方法 变为 特性（属性）
    def Bar(self):
        #print self.Name
        return 'someting'

hb = Province('河北','何家庄','李杨')    ####封装为对象hb
sb = Province('上海','济南','李杨')

print hb.Capital
print sb.Capital

print Province.memo   #访问类变量

###讲一下self

## 何为字段，何为方法
##属于类的字段 都叫静态字段
##属于对象的字段，都叫动态字段
#==============

##假设通过类来访问动态字段，是不可以的
#print Province.Name

##动态字段可不可以访问静态字段？ 可以
print hb.memo           ###个人建议  最好别通过动态字段来访问静态，会造成歧义

hb.sports_meet()

###类可以访问动态方法么，不可以，此时应该考虑静态方法
##静态方法和外部的函数是一模一样，唯一的区别就是从逻辑上属于这个类而已

Province.Foo()

hb.Bar


###类有三种结构，字段、方法、特性（属性）


#####类的目的 对某个类别做个抽象




class MsSqlHelper:
    conn = ''

    @staticmethod
    def add(sql):
        pass

    @staticmethod
    def delete(sql):
        pass

    @staticmethod
    def update(sql):
        pass

    @staticmethod
    def select(sql):
        pass




###########多态、封装的意义也是面向对象的意义，方法相同，对于第三方来说 不需要知道你们的名字，只需要叫你做事
### 这就是面向对象的精髓


###  在python中  函数式编程非常强大   也能实现多态，关键原因就是它没有静态约束（定义2个module，里面的方法名字一样）
#### python的反射机制，可以100%等于面向对象（假设没有反射，面向对象对python是有意义的）

###在真正的面向对象语言中，要做到过程式编程实现多态，非常困难，例如java 强制类型静态约束


###面向对象： 我想干一个事业
###过程式： 我想做一件事情，面对于复杂的程序，修改起来很复杂
