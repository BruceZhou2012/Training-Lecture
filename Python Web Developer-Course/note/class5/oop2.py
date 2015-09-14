#coding:utf-8

__author__ = 'gubaoer'

####私有方法和私有字段


class Province(object):
    memo = '23 number'     ##类变量

    def __init__(self,name,capital,leader,flag):
        self.Name = name          ### self.xxxx属于对象变量
        self.Capital = capital
        self.Leader = leader
        self.__Thailand = flag    ###私有字段

    def sports_meet(self):        #### 动态方法
        print self.Name + '正在开运动会'


    @staticmethod            ###静态方法，属于类
    def Foo():
        print '省要带头反腐'

    @property                ### 动态方法 变为 特性（属性）
    def Bar(self):
        #print self.Name
        return 'someting'

    def show(self):
        print self.__Thailand    ##这样就可以访问得到私有字段

    def __sha(self):     ###私有方法
        print 'hello'

    def Foo2(self):
        self.__sha()   ##访问私有方法


    @property
    def Thailand(self):
        return self.__Thailand          ####还可以用property装饰器来访问私有方法,只读

    @Thailand.setter                    ####只写特性
    def Thailand(self,value):
        self.__Thailand = value


###外部访问、内部访问

japan = Province('日本','济南','gubaoer',True)
# print japan.__Thailand
japan.show()
#japan.__sha()
japan.Foo2()
print japan.Thailand
japan.Thailand = False
print japan.Thailand



