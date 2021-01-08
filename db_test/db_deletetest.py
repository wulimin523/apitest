# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :db_deletetest
# @Date     :2021/1/4 16:28
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import pymysql

# 建立数据库连接
conn = pymysql.Connect(host="datum.sys",
                       user="root",
                       password="Aa@123456",
                       database="ocpcloudpro",
                       port=0,
                       charset='utf8',
                       autocommit=True)
cursor = conn.cursor()
row = cursor.execute("DELETE FROM hb_app_sm_code WHERE APP_MOBILE_NUM = '18612701156'")
print("受影响的条数：", row)

cursor.close()
conn.close()