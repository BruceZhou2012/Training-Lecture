#coding:utf8
'''
class A(object):
    def func(self):
        print 'func'

    def func2(self,msg):
        print 'msg'

a = A()
a.func()
a.func2('Python')
'''
'''
class A(object):
    author = "Guido"
    def __init__(self,page):
        self.page = page
    @classmethod
    def class_method(cls,name):
        return "[" + name + "]"
    @staticmethod
    def static_method(name):
        return "[" + name + "]"

print A.class_method("python")
print A.static_method("haha")

book_a = A(10)
book_b = A(200)

book_a.author = "gubaoer"  ###此时是创建了一个实例变量
print book_a.author
print book_b.author

print book_a.page
print book_b.page
'''
'''
class A(object):
    def __init__(self,_id):
        self.id = _id
        print 'A'

class B(A):
    def __init__(self,_id):
        super(B,self).__init__(_id)
        print _id


b = B(1)
'''
'''
class C(A,B):
    pass
    '''
'''
class A(object):
    """
        doc
    """
    name = 'A'
    def __init__(self,_id):
        self.id = _id
        print 'A'

    def msg(self):
        print 'msg'

print dir(A)
print A.__dict__
print A.__doc__
'''
'''
class A(object):

    name = "A"
    def __init__(self,_id):
        self.__id = _id

    def msg(self):
        print self.__id

a = A(1)
a.name = "Python"
#print a.__id
print a.__dict__
print a.msg()
'''

'''

class A:

    def __init__(self,_id):
        self.name = _id
    def msg(self):
        print self.__id

print getattr(A,"msg")
'''