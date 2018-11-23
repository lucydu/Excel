import mysql.connector
from common import pro_path
from common.read_config import ReadConfig

class DoMysql:
    def do_mysql(self,query_sql,state=1):
        #2：链接数据库 调用connect方法 会产生一个链接
        config=eval(ReadConfig().read_config(pro_path.conf_path,'DATABASE','config'))
        cnn=mysql.connector.connect(**config) #3:生成一个游标  获取操作数据的权限
        cursor=cnn.cursor()
        cursor.execute(query_sql) #4：利用游标去查询数据
        if state==1:#5:利用游标获取查询结果  fetchone() fetchall()
             res=cursor.fetchone()#返回的数据类型是元组
        else:
             res=cursor.fetchall()#返回的数据类型是列表,里面的元素是元组
        cursor.close()#6:操作完毕 就要关闭游标
        cnn.close()  #7：断开链接
        return res

if __name__ == '__main__':

        # sql='select mobilephone from member where id<23505'
        # sql_list=['select mobilephone from member where id<23505',
        #           'select mobilephone from member where id<23504']
        # for item in sql_list:
        #     res=DoMysql().do_mysql(config,item,0)
        #     print(res)

        query='select max(mobilephone) from  member'
        result=DoMysql().do_mysql(query)
        print(result[0])