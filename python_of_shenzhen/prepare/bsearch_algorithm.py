def search(object, args):
    def bSearch(object, args, low, hight):

        print object

        print(low,hight)

        if hight == low:
            return object[low] == args

        mid = (hight + low) // 2
        print mid

        if object[mid] == args:
            return True

        elif object[mid] > args:
            return bSearch(object, args, low, mid - 1)
        else:
            return bSearch(object, args, mid + 1, hight)
    if len(object) == 0:
        return False
    else:

        return bSearch(object, args, 0, len(object) - 1)

print search([1], 3)