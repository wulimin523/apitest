# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :dbtest
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
                       charset='utf8')
cursor = conn.cursor()
row = cursor.execute("SELECT * from hb_card_card where CARD_NO like '20201%'")
print("受影响的条数：", row)
# 获取一条
print( cursor.fetchone() )
# 获取指定条数
print(cursor.fetchmany(2))
# 获取剩余所有条数
print(cursor.fetchall())

cursor.close()
conn.close()