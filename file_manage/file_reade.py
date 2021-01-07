# -*- coding: utf-8 -*-

import xlrd

# 导入需要读取的第一个Excel表格的路径
data1 = xlrd.open_workbook(r'E:\\practice\\Python\\user.xlsx')
table = data1.sheets()[0]
# print(table)
# 创建一个空列表，存储Excel的数据
tables = []


# 将excel表格内容导入到tables列表中
def import_excel():
    for rown in range(1, table.nrows):
        array = {'userName': '', 'userCnName': '', 'newPwd': '', 'phone': '', 'email': '',
                 'team':'', 'code':'', 'melu':''}
        array['userName'] = table.cell_value(rown, 0)
        array['userCnName'] = table.cell_value(rown, 1)
        array['newPwd'] = table.cell_value(rown, 2)
        array['phone'] = str(int(table.cell_value(rown, 3)))
        array['email'] = table.cell_value(rown, 4)
        array['team'] = table.cell_value(rown, 5)
        array['code'] = table.cell_value(rown, 6)
        array['melu'] = table.cell_value(rown, 7)
        tables.append(array)
    # print("tables:", tables)
    return tables



if __name__ == '__main__':
    # 将excel表格的内容导入到列表中
    import_excel()

# print(c)
