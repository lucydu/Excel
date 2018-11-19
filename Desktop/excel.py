# coding=utf-8
import xlrd
import xlwt
import xlutils.copy
# #打开excel
# 路劲：/Users/admin/Desktop/Auto/PycharmProjects/mobile/xxx.xlsx
# excel = xlrd.open_workbook('xxx.xlsx')
# 打印出所有的excel
#
# sheet_name = excel.sheet_names()
# print (sheet_name)
#
# 遍历所有sheet_name
# 读取表格内的数据
# for i in sheet_name:
#     print (i)
#     sheet_data = excel.sheet_by_name(u'%s'%i)
#     num_rows = sheet_data.nrows
#     for curr_row in range(1,num_rows):
#       row = sheet_data.row_values(curr_row)
#       case_name = row[3]
#       data = row[4]
#       print ("用例名称：%s 请求参数：%s"%(case_name,data))
def read(sheet_name):
    excel = xlrd.open_workbook('xxx.xlsx')
    sheet_data = excel.sheet_by_name(u'%s'%sheet_name)
    num_rows = sheet_data.nrows
    for curr_row in range(1,num_rows):
      row = sheet_data.row_values(curr_row)
      case_name = row[3]
      data = row[4]
      # print ("用例名称：%s 请求参数：%s"%(case_name,data))
      return case_name,data

def write(raw,col,data):
    excel = xlrd.open_workbook('xxx.xlsx')
    wb = xlutils.copy.copy(excel)
    ws = wb.get_sheet('device')
    ws.write(raw,col,data)
    wb.save('xxx.xlsx')
    return()

# sheet.write('2','0','D_002')
# sheet.save('xxx.xlsx')

