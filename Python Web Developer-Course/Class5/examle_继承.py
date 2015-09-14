 #coding:utf-8


'''
class Father(object):

    def __init__(self,):
        self.hire = '头发很茂密'
        self.__sex = '父亲是同性恋'

    def Bad(self):
        print '吸毒'

    def __slot__(self): #限制这个类的某个动态方法
        pass


class Son(Father):  ## 子类

    def __init__(self):
        super(Son,self).__init__()    ### 继承了父亲的构造函数定义的所有属性
        self.size = "强壮"

    def Bad(self):   ##覆盖
        print '赌博'
        Father.Bad(self)

gubaoer = Son()
gubaoer.Bad()
'''

class A:
    def __init__(self):
        print '我是父亲'
    def bad(self):
        print '杀人'
    def good(self):
        print '父亲是好人'

class B(A):
    def __init__(self):
        print 'my name is son1'
    def bad(self):
        print '赌博'

class C(A):
    def __init__(self):
        print 'my name is son2'

    def bad(self):
        print '偷鸡摸狗'

    def good(self):
        print '好人'

class grandson(B,C):
    pass

gubaoer = grandson()
gubaoer.bad()
print gubaoer.good()
















