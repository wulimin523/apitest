# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :test01_login
# @Date     :2021/1/5 15:12
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import requests

from api.api_department import ApiDepartment
from api.api_login import ApiLogin
from tool.read_json import read_json
from parameterized import parameterized
from utils import assert_common
import app
import logging
def get_data():
    arrs = []
    arrs.append(tuple(read_json('login1_post.json').values()))
    print( arrs )
    return arrs

def get_data_all():
    arrs = []
    arrs.append(tuple(read_json( "dp_getall.json" ).values()))
    print(arrs)
    return arrs

class TestLogin():
    session = None
    @classmethod
    def setup_class(cls) -> None:
        # 获取session对象
        cls.session = requests.session()
        # 创建ApiLogin实例
        cls.apilogin = ApiLogin(cls.session)
        cls.dp = ApiDepartment( cls.session )

    @classmethod
    def teardown_class(cls) -> None:
        # 关闭session
        cls.session.close()
    @parameterized.expand(get_data())
    def test01_post_login(self, data, status_code, resultCode, resultMsg):
        # 调用登录业务方法
        url = app.HOST + "service?optType=0&cdsName=login"
        response = self.apilogin.api_post_login(url, app.HEADERS, data)
        app.TOKEN = response.json().get('resultObj').get('token')
        # 断言
        assert_common(self, response, status_code, True, resultCode, resultMsg)
        logging.debug("登陆成功接口返回的数据为： {}".format(response.json()))

    # @parameterized.expand( get_data_all() )
    # def test02_getall(self, data, status_code, resultCode, resultMsg):
    #     # 给请求接口添加token
    #     app.HEADERS['authorization'] = app.TOKEN
    #     r = self.dp.api_get_all_dp( app.HEADERS, data)
    #     # 断言
    #     assert_common( self, r, status_code, True, resultCode, resultMsg )
    #     print("获取项目列表接口返回成功，返回的数据为：{}".format(r.json()))


# if __name__ == '__main__':
#     unittest.main()
