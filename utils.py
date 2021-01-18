# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :utils
# @Date     :2021/1/6 16:42
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
def assert_common(self, response, http_code, success, code, message):
    assert http_code, response.status_code  # 断言响应状态码
    # self.assertEqual( success, response.json().get("success"))  # 断言success
    assert code == response.json().get("resultCode")  # 断言code
    assert message in response.json().get("resultMsg")  # 断言message

