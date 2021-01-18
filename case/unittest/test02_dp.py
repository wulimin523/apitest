# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :test02_dp
# @Date     :2021/1/5 17:27
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest
import requests
import json

import app
from api.api_department import ApiDepartment
from parameterized import parameterized
from tool.read_json import read_json
from utils import assert_common


def get_data_post():
    arrs = []
    arrs.append(tuple(read_json( "dp_post.json" ).values()))
    return arrs
def get_data_put():
    arrs = []
    arrs.append(tuple(read_json( "dp_put.json" ).values()))
    return arrs

def get_data_all():
    arrs = []
    arrs.append(tuple(read_json( "dp_getall.json" ).values()))
    return arrs

def get_data_one():
    arrs = []
    arrs.append(tuple(read_json( "dp_getone.json" ).values()))
    return arrs

def get_data_delete():
    arrs = []
    arrs.append(tuple(read_json( "dp_delete.json" ).values()))
    return arrs
class TestDP(unittest.TestCase):
    session = None
    # 初始化
    @classmethod
    def setUpClass(cls) -> None:
        # 获取session对象
        cls.session = requests.session()
        # 获取apiDP对象
        cls.dp = ApiDepartment(cls.session)
    # 结束
    @classmethod
    def tearDownClass(cls) -> None:
        cls.session.close()
    # 新增方法
    # @parameterized.expand(get_data_post())
    # def test01_post_dp(self, data):
    #     # rep = self.dp.api_post_dp(data)
    #     # print(rep)
    #     print(data)
    # 更新方法
    def test_put_dp(self):
        pass
    # 查询所有方法
    @parameterized.expand( get_data_all())
    def test02_getall(self, data, status_code, resultCode, resultMsg):
        # 给请求接口添加token
        app.HEADERS['authorization'] = app.TOKEN
        r = self.dp.api_get_all_dp( app.HEADERS, data )
        # 断言
        assert_common( self, r, status_code, True, resultCode, resultMsg )
        print( "获取项目列表接口返回成功，返回的数据为：{}".format( r.json() ) )
    # 查询指定方法
    def test_getone(self):
        pass
    # 删除方法
    def test_delete(self):
        pass

if __name__ == '__main__':
    unittest.main()
