__author__ = 'zz'
#主程序执行入口
import unittest
import HTMLTestRunnerNew
from common import pro_path
from common.send_email import sendEmail
from common.test_http_request import TestHttpRequest


suite=unittest.TestSuite()
#ddt 加载用例 loader
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

#生成测试报告 HTML
with open(pro_path.test_report_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,
                                            title='0901python 9期测试报告',
                                            description='前程贷接口的测试',
                                            tester='华华')
    runner.run(suite)

#添加发送邮件的请求
sendEmail().send_email('746674534@qq.com',pro_path.test_report_path)
sendEmail().send_email('505978451@qq.com',pro_path.test_log_path)