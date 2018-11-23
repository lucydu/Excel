# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 20:37
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_0904.py
import requests

login_url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
login_data={'mobilephone':'15096090551','pwd':'123456'}

recharge_url='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
recharge_data={'mobilephone':'15096090551','amount':'1000'}

#session的方式
# s=requests.session()#产生一个会话
# res=s.get(login_url,params=login_data).json()
# res_1=s.post(recharge_url,recharge_data).json()
# print('登录结果是{0}'.format(res))
# print('充值结果是{0}'.format(res_1))

# cookie的方式--优先推荐
#登录请求
response=requests.get(login_url,login_data,cookies={})
res=response.json()#获取响应结果
cookies=response.cookies#获取对应的cookie
print('登录结果是{0}'.format(res))
print('登录成功后产生的cookies是{0}'.format(cookies))
#cookie他是类似于字典格式
# print('JSESSIONID:   {0}'.format(cookies['JSESSIONID']))

#充值结果
res_1=requests.get(recharge_url,recharge_data,cookies=cookies).json()
print('充值结果是{0}'.format(res_1))

#状态处理：每次请求 服务器都要检验你的状态
#cookie  session
#本地cookie session_id
#服务器 session 会话  会话时间
#每次提交请求的时候 会随带cookie  发送至服务器 检查会话是否已过期
#当你在同一个会话下面  你可以直接请求

#token是什么？鉴权  请求参数  header


#手机号码参数  化的问题--怎样让手机自动的变化
#1：随机数？138
#2：时间戳
#3：把数据存在Excel 0550-->利用到用例  +1-->写回到excel里面
#4：如果你又数据库的操作权限 且手机号码未加密
# 利用sql查询当前库里面最大的手机号 在这个基础上+1

