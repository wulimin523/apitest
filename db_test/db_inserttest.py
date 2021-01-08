# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :db_inserttest
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
row = cursor.execute("INSERT INTO hb_app_sm_code VALUES('18612701156','2020-09-07 19:09:23',0,'123456')")
print("受影响的条数：", row)

cursor.close()
conn.close()