# [1,2,3,4,5,6]

def search(object, keyword):

    def Bsearch(object, keyword, min, max):

        if min == max:
            return object[min]==keyword

        mid = (min+max) // 2
        print object
        print (min, mid, max)
        if object[mid] == keyword:
            return True
        elif object[mid] > keyword:
            return Bsearch(object, keyword, min, mid-1)
        else:
            return Bsearch(object, keyword, mid+1, max)

    return Bsearch(object, keyword, 0, len(object)-1)


d = [1,2,3,4,5]
print search(d, 5)