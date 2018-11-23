__author__ = 'zz'
#这个文件存储的都是绝对路径
import os

project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件的路径：
conf_path=os.path.join(project_path,'conf','auto_test.conf')

#测试数据的路径
test_data_path=os.path.join(project_path,'test_data','test_cases.xlsx')

#测试报告的路径
test_report_path=os.path.join(project_path,'test_result','html_report','test_report.html')

#测试日志记录的路径
test_log_path=os.path.join(project_path,'test_result','log','test_log.txt')
