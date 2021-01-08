# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :api_login
# @Date     :2021/1/5 13:55
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests
class ApiLogin(object):
    def __init__(self, session):
        self.session = requests.session()
    def api_post_login(self, url, headers, data):
        return self.session.post(url=url,headers=headers, json=data)


