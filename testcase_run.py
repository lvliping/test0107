from unittest import TestCase, TestSuite, TextTestRunner
import unittest
from tools.HTMLTestRunner_cn import HTMLTestRunner
import time
import traceback
import sys
import os

current_path = os.getcwd()  # 获取当目录
sys.path.append(current_path)
paths = sys.path
for p in paths:
    print(p)
# 加载测试用例, 第一个参数是要加载的测试用例，用例类文件所在的目录，
# 子目录也会加载    pattern参数是加载指定格式python文件名的用例
testcase_path = current_path + "/testcase"  # 拼接测试用例所在的目录
suite = unittest.defaultTestLoader.discover(testcase_path, pattern='*.py')
# runner = TextTestRunner()
# runner.run(suite)
now_time = time.strftime("%Y-%m-%d %H %M %S", time.localtime())  # 生成一个年月日时分秒的时间戳
reports_path = current_path + "/reports/重庆银行自动化测试报告" + now_time + ".html"  # 生成报告存放的目录
print("reports_path", reports_path)
file = None
try:
    file = open(reports_path, "wb")
    runner = HTMLTestRunner(stream=file, title="重庆银行接口测试用例报告", verbosity=2, description="接口测试用例执行情况")
    runner.run(suite)  # 把缓冲区中的数据写入到文件中
    file.flush()
except:
    print("运行错误")
    print(traceback.format_exc())
finally:
    if file:
        file.close()
print("执行结束")
