# [1,2,3,4,5]  2

def search(object, keyword):
    def bSearch(object, keyword, min, max):

        if min == max:
            return object[min] == object

        mid = (min + max) // 2

        if object[mid] == keyword:
            return True
        elif object[mid] > keyword:
            return bSearch(object, keyword, min, mid - 1)
        else:
            return bSearch(object, keyword, mid + 1, max)

    if len(object) < 1:
        return False
    else:
        return bSearch(object, keyword, 0, len(object) - 1)

print search([1,2,3,4,5], 5)