#coding:utf-8
import urllib


class AliveError(Exception):

        def __init__(self, msg):
                self.message = msg


class DownloadClient(object):
    
        def __init__(self, url, store_path):
                self.url = url
                self.store_path = store_path
        
        def openurl(self):
                scripturl = urllib.urlopen(self.url, self.store_path)
                return scripturl

        def gethead(self):
                scriprurl = self.openurl()
                check_server = scriprurl.info().getheader('server')
                return check_server

        def run(self):
                try:
                    if self.gethead() is None:
                            assert AliveError("远程调用出错")
                except AliveError, e:
                        print e.message
                except IOError:
                        print '网络问题'
                else:
                    urllib.urlretrieve(self.url, self.store_path)

if __name__ == "__main__":
        # x = DownloadClient('http://10.32.119.228:81/opbin/auto_roleback/roleback-messer-resource.sh','C:/dd.txt')
        x = DownloadClient('http://picture.youth.cn/qtdb/201307/W020130726409830540588.jpg', 'C:/dd.jpg')
        x.run()