# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :apitest
# @File     :run_suite
# @Date     :2021/1/5 18:12
# @Author   :吴利民
# @Email    :wulimin523@163.com
# @Software :PyCharm
-------------------------------------------------
"""
import unittest
from tool.HwTestReport import HTMLTestReport
from case.unittest.test01_login import TestLogin
from case.unittest.test02_dp import TestDP

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDP))

with open('../report/report.html', 'wb') as f:
    HTMLTestReport(stream=f).run(suite)
