__author__ = 'zz'
import unittest
import logging
from ddt import ddt,data
from common import pro_path
from common.do_excel import DoExcel
from common.do_mysql import DoMysql
from common.http_request import HttpRequest
from common import  my_logger


#获取测试数据
test_data=DoExcel(pro_path.test_data_path).do_excel()

COOKIES={}#全局变量cookie的初始值
LOAN_ID=''#全局变量loanid的初始值
LOAN_MEMBER_ID='23523'#存储借款用户的memberid
INVEST_MEMBER_ID=''#存储投资用户的member_id

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        self.t=DoExcel(pro_path.test_data_path)#创建一个实例

    # @data(*test_data_1)
    # def test_invest(self,item):#专门测试投资接口
    #     pass#

    @data(*test_data)
    def test_api(self,item):#回归测试
        global  COOKIES#声明全局变量，必要的时候去更新从cookie的值
        global  LOAN_ID
        global INVEST_MEMBER_ID
        logging.info("正在执行第{0}条用例：{1}".format(item['CaseId'],item['Title']))
        logging.info("发起请求的地址是：{0}".format(item['URL']))


        #在http请求之前 要完成item['Param'] 参数替换 loan_id
        if item['Param'].find('${loan_id}')!=-1:
            new_param=item['Param'].replace('${loan_id}',str(LOAN_ID))
            if new_param.find('${member_id}')!=-1:
                new_param=new_param.replace('${member_id}',str(INVEST_MEMBER_ID))
        else:
            new_param=item['Param']

        logging.info("发起请求的参数是：{0}".format(new_param))
        res=HttpRequest().http_request(item['URL'],eval(new_param),item['Method'],COOKIES)

        #查询loan_id 必须放在http请求之后
        # if item['Params'].find("memberId")!=-1:
        #     member_id=eval(item['Params'])['memberId']
        #     #查询该用户添加的标的最大的那个
        #     query_loan_id='select max(id) from loan where memberId={0}'.format(member_id)
        #     LOAN_ID=DoMysql().do_mysql(query_loan_id)[0]

        #查询member_id 根据手机号去查询？
        if INVEST_MEMBER_ID=='':#为什么要加一个这样的if判断？ 之后就不需要再去替换
            query_member_id='select id from member where mobilephone={0}'.format(eval(item['Param'])['mobilephone'])
            member_id=DoMysql().do_mysql(query_member_id)[0]
            INVEST_MEMBER_ID=member_id

        #第二种简单的方法去处理loan_id:
        query_loan_id='select max(id) from loan where memberId={0}'.format(LOAN_MEMBER_ID)
        loan_id=DoMysql().do_mysql(query_loan_id)[0]
        logging.info("获取到的loanid{0}".format(loan_id))
        if loan_id:#当数据不为空的时候 就进行数据的替换
            LOAN_ID=loan_id#替换

        #登录请求之后会产生一个cookie？
        if res.cookies!={}:#如果cookie不为空 就对全局变量进行修改
            COOKIES=res.cookies

        #断言：
        try:
            self.assertEqual(item['ExpectedResult'],int(res.json()['code']))
            TestResult='PASS'#存储测试用例的执行结果 通过是pass  失败是Fail
        except Exception as e:
            logging.error("断言出错了，错误是：{0}".format(e))
            TestResult='FAIL'
            raise e#处理完毕之后 要raise错误
        finally:
            self.t.write_back('test_data',item['CaseId']+1,7,str(res.json()))#因为Excel里面只能支持传递字符串 整数，所以这里要强制转一下
            self.t.write_back('test_data',item['CaseId']+1,8,TestResult)





