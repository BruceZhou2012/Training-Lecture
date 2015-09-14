import urllib

class MyException(Exception):

    def __init__(self,msg):
        self.message = msg
        print self.message

class Wget_API(object):

    def __init__(self, url, local_path):
        self.url = url
        self.local_path = local_path

    def openurl(self):
        url_obj = urllib.urlopen(self.url)
        return url_obj

    def gethead(self):
        is_alive = self.openurl().info().getheader('server')
        return is_alive

    def download(self):
        try:
            if self.gethead() is None:
                assert MyException('Server is deaded')
        except MyException, e:
                print e.message
        else:
            urllib.urlretrieve(self.url,self.local_path)

if __name__ == '__main__':
    x = Wget_API('http://h.hiphotos.baidu.com/image/pic/item/9825bc315c6034a8d141851dce1349540823768e.jpg','D:\AV.jpg')
    x.download()
