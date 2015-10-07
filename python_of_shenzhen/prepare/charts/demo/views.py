# coding: utf-8

import json
import random
from collections import Counter

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

"""
[
                                    {value: 335, name: '直接访问'},
                                    {value: 310, name: '邮件营销'},
                                    {value: 234, name: '联盟广告'},
                                    {value: 135, name: '视频广告'},
                                    {value: 1548, name: '搜索引擎'}
                                ]

"""


class Demo(View):
    def get(self, request):
        return render(request, 'demo/demo.html')


class get_graphy(View):
    def get(self, request):
        dd = [random.choice(("上海", "广州", "深圳", "北京")) for i in range(1, 20)]
        xx = dict(Counter(dd))
        vv = json.dumps(xx)
        zz = dict(haha=[{'value': 335, 'name': '上海'},
                        {'value': 310, 'name': '北京'}
                        ],
                  city=['上海', '北京'])

        print zz
        c = {'haha':[], 'city':["上海", "广州", "深圳", "北京"]}
        for k ,v in xx.iteritems():
            c['haha'].append({'value': v, 'name':k})
        print c
        return HttpResponse(json.dumps(c))
