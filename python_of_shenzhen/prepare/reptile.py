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
ddd = s.get("http://wx.233.com/uc/account/user/info")