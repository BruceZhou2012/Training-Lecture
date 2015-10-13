# coding: utf-8
import requests
import re
'''
dd = requests.post('http://wx.233.com/account/login', data={'username': 'gubaoer', 'passwd': '123456'})

data = dd.text

link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", data)  # 直接把href=""或href=''之间的信息获取到

for url in link_list:
    print url
'''
s= requests.session()
d = s.post("http://wx.233.com/account/login/auditaccount/", data={'userName':'gubaoer', 'passwd':'123456'})
html_obj = s.get("http://wx.233.com/account/")




'''

import bs4
html = html_obj.text
html = html.encode('utf-8')
soup = bs4.BeautifulSoup(html)
links = soup.select('dl.my-friend-dl a.greenTxt')
for i in links:
    print i.get_text()
'''