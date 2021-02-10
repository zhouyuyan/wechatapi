# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 10:54 下午
# @Author  : zhouyy
# @FileName: we_work.py
# @Software: PyCharm
import requests

import pytest
class Wework:
    def get_token(self):
        data = {
            "corpid": "ww1c02382c8f56d651",
            "corpsecret":"YH3-ZsAgWMwKSvJjmh8CUUSLLX2QeUhE17LAOQtntMw"
        }

        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",data)

        return r.json()['access_token']
    def get_session(self):
        s = requests.Session()
        s.params = {
            "access_token": self.get_token()
        }
        return s
