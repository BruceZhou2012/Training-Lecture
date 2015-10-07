# coding: utf-8
__author__ = 'boylegu'

'''
class Factory(object):
    def createFruit(self, fruit):
        if fruit == "apple":
            return Apple()

        elif fruit == "banana":
            return Banana()


class Fruit(object):
    def __str__(self):
        return "fruit"

class Apple(object):
    def __str__(self):
        return "apple"

class Banana(Fruit):
    def __str__(self):
        return  "banana"

factory = Factory()
print factory.createFruit("apple")

'''

'''

class Fruit(object):

    def __init__(self):
        self.__color="red"


class Apple(Fruit):
    pass

fruit = Fruit()
apple = Apple()
print Apple.__bases__
print Fruit.__bases__
print apple.__dict__
print Apple.__module__
'''

'''
# 单例模式

class Singleton(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls, *args, **kwargs)

        return Singleton.__instance


class Fruit(object):
    def __init__(self, color="red", price=0):
        self.__color = color
        self.__price = price

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


fruit = Fruit("blue", 10)
print fruit.__dict__.get("_Fruit__color")


class FruitShow(object):
    def __getitem__(self, item):
        return self.fruits[item]


shop = FruitShow()
shop.fruits = ["a", "b"]
print shop[1]
'''

class Fruit(object):
    def __init__(self, price=None):
        self.price = price

    def __add__(self, other):
        return self.price + other.price

    def __gt__(self, other):

        if self.price > other.price:
            flag = True
        else:
            flag = False

        return flag


class Apple(Fruit):
    pass


class Banana(Fruit):
    pass


apple = Apple(3)
print apple.price

banana = Banana(2)
print banana.price

total = apple + banana
print total
