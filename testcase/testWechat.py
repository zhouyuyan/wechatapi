# -*- coding: utf-8 -*-
# @Time    : 2021/2/10 11:10 下午
# @Author  : zhouyy
# @FileName: testWechat.py
# @Software: PyCharm
import json

from we_work import Wework
import pytest


# response1 = session.get(url,params,headers)
# response2 = session.post(url,data,json,headers)
class TestWechat:
    def setup(self):
        self.s = Wework().get_session()

    def create(self, userid, name, mobile, department):
        data = {

            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department

        }
        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/create", json=data)
        assert r.json()['errmsg'] == 'created'

    def get(self, userid):
        param = {
            "userid": userid
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get", params=param)

        print(f"name={r.json()['name']}")

    def updata(self, userid, name):
        data = {
            "userid": userid,
            "name": name
        }
        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/update", json=data)
        # print(r.json())
        assert r.json()['errmsg'] == 'updated'

    def delete(self, userid):
        param = {
            "userid": userid
        }

        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/delete", params=param)
        assert r.json()["errmsg"] == "deleted"

    def get_simplelistf(self, department_id):
        param = {
            "department_id": department_id
        }
        r = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/simplelist", params=param)
        print(r.json()['userlist'])
        res = []
        for element in r.json()['userlist']:
            if element['userid'] != "ZhouYuYan":
                res.append(element['userid'])
        print(res)
        self.useridlist = res
        return self.useridlist

    def batchdelete(self, useridlist):
        data = {
            "useridlist": useridlist
        }
        r = self.s.post("https://qyapi.weixin.qq.com/cgi-bin/user/batchdelete", json=data)
        assert r.json()["errmsg"] == "deleted"

    def test_create(self):
        userid = "test01"
        name = "111"
        mobile = "17605888000"
        department = [1]

        # self.create(userid,name,mobile,department)
        # self.get(userid)
        # self.updata(userid,"222")
        # self.get(userid)
        # self.delete(userid)

        self.get_simplelistf(department)
        if  len(self.get_simplelistf(department)):
            self.batchdelete(self.useridlist)
        else:
            print("没有可批量删除的成员")
