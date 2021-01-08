# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :db_trantest
# @Date     :2021/1/4 18:37
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
# row = cursor.execute("INSERT INTO hb_app_sm_code VALUES('18612701158','2020-09-07 19:09:23',0,'123456')")
# print("受影响的条数：", row)
#
# row = cursor.execute("UPDATE hb_app_sm_code SET VERIFICATION_CODE = '125987' where APP_MOBILE_NUM = '18612701158'")
# print("受影响的条数：", row)



try:
    row = cursor.execute( "INSERT INTO hb_app_sm_code VALUES('18612701161','2020-09-07 19:09:23',0,'123456')" )
    print( "受影响的条数：", row )

    row = cursor.execute(
        "UPDATE hb_app_sm_code SET VERIFICATION_CODE = '125987' where APP_MOBILE_NUM = '18612701161'" )
    print( "受影响的条数：", row )
    # 自动提交事务
    # conn.autocommit(True)
    # 手动提交事务
    conn.commit()
except Exception as e:
    # 手动回滚事务
    conn.rollback()
finally:
    cursor.close()
    conn.close()