__author__ = 'boylegu'


def y(object):
    def x(object, i):
        try:
            print object[i]
        except IndexError:
            return object[-1]
        return x(object[i:], i + 1)

    return x(object, 0)


print y([1, 2, 3])
