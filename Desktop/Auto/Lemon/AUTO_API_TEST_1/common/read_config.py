__author__ = 'zz'
import configparser

#配置文件类
class ReadConfig:
    def read_config(self,conf_file,section,option):
        cf=configparser.ConfigParser()
        cf.read(conf_file)
        value=cf.get(section,option)
        return value#返回读取的配置值

if __name__ == '__main__':
    flag=ReadConfig().read_config('auto_test.conf','TESTCASE','flag')
    print(flag)