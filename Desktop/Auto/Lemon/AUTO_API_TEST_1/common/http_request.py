__author__ = 'zz'
#写个接口类：专门完成接口测试
import requests
import logging
from common import my_logger

class HttpRequest:
    def http_request(self, url, param, method,cookies):
        if method.upper() == 'GET':#防止我们自己输入不分大小写 写错
            try:
                response = requests.get(url, param,cookies=cookies)
            except Exception as e:
                logging.error("GET请求出错了：{0}".format(e))
                raise e#抛出错误
        else:#
            try:
                response = requests.post(url, param,cookies=cookies)
            except Exception as e:
                logging.error("POST请求出错了：{0}".format(e))
                raise e#抛出错误
        return response


#测试代码：
if __name__ == '__main__':
    url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    param={'mobilephone':'15096090551','pwd':'123456','regname':'test_python9'}

    res=HttpRequest().http_request(url,param,'get')
    print("http请求返回的结果是：{0}".format(res))

