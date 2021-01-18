# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :api_department
# @Date     :2021/1/5 17:05
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import api
import app
class ApiDepartment():
    def __init__(self, session):
        self.session = session
    # 获取所有参与项目
    def api_get_all_dp(self, headers, data):
        return self.session.get(url=app.HOST+"service?optType=1&cdsName=clockHours", headers=headers, json=data)
    # 获取单个
    def api_get_one_dp(self, dpid):
        return self.session.get(api.url_itime + dpid +'/')
    # 新增某个
    def api_post_dp(self, data):
        return self.session.post(api.url_itime, json=data)
    # 更新某个
    def api_put_dp(self, dpid, data):
        return self.session.put(api.url_itime + dpid +'/', json=data)
    # 删除某个
    def api_delete(self, dpid):
        return self.session.delete(api.url_itime + dpid +'/')
