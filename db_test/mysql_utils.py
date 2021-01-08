# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :mysql_utils
# @Date     :2021/1/4 18:52
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest

import pymysql


class MysqlUtil(unittest.TestCase):
    conn = None
    cursor = None
    # 获取连接对象方法
    def get_conn(self):
        self.conn = pymysql.Connect(host="datum.sys",
                       user="root",
                       password="Aa@123456",
                       database="ocpcloudpro",
                       port=0,
                       charset='utf8')
        return self.conn

    # 获取游标
    def get_cursor(self):
        return self.get_conn().cursor()

    # 关闭游标
    def close_cursor(self, cursor):
        cursor.close()

    # 关闭数据库连接
    def close_conn(self):
        self.conn.close()

    def test_fetchall(self, sql):
        self.cursor = self.get_cursor()
        try:
            self.cursor.execute( sql )
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.close_cursor( self.cursor )
            self.close_conn()

    def test_update(self, sql):
        self.cursor = self.get_cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
        finally:
            self.close_cursor(self.cursor)
            self.close_conn()


