# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :db_mysqltest
# @Date     :2021/1/4 19:18
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
from db_test.mysql_utils import MysqlUtil

fetchsql = "SELECT * from hb_card_card where CARD_NO like '20201%'"
mysqlutil = MysqlUtil()
print(mysqlutil.test_fetchall(fetchsql))

# deletesql = "DELETE FROM hb_app_sm_code WHERE APP_MOBILE_NUM = '18612701523'"
# mysqlutil = MysqlUtil()
# print(mysqlutil.test_update(deletesql))