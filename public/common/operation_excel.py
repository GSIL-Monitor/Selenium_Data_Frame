"""
__author__ = 'LZL'
__mtime__ = '2018/8/6'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

import xlrd
from xlutils import copy

class OperationExcel:

    def __init__(self, excel_path, sheet_index):
        '''
        获取sheet对象
        @param excel_path: excel文件路径
        @param sheet_index:  sheet的索引
        '''
        self.excel_path = excel_path
        self.sheet_index = sheet_index
        self.sheet_data = self.get_sheet()


    def get_sheet(self):
        '''
         获取sheet
        :return:
        '''
        excel = xlrd.open_workbook(self.excel_path)
        return excel.sheet_by_index(int(self.sheet_index))

    def get_rows(self):
        '''
        获取sheet中的所有行数
        :return:
        '''
        return self.sheet_data.nrows

    def get_cols(self):
        '''
        获取列数
        :return:
        '''
        return self.sheet_data.ncols


    def get_value(self, row, col):
        '''
        获取单元格内容
        :param row: 行
        :param col: 列
        :return:
        '''
        return self.sheet_data.cell_value(rowx=row, colx=col)

    def write_data(self, row, col, data=None):
        '''
        写入内容：复制、写入、保存
        @param row: 行
        @param col: 列
        @param data: 内容
        @return:
        '''
        # 复制
        new_excel = copy.copy(xlrd.open_workbook(self.excel_path))
        # 写入
        new_excel.get_sheet(self.sheet_index).write(row, col, data)
        # 保存
        new_excel.save(self.excel_path)


    def get_data_for_cols(self, col):
        '''
        获取列的内容
        @param col: 列
        @return:
        '''
        return self.sheet_data.col_values(col)

    def get_row_data(self, row):
        '''
        获取行的内容
        @param row: 行
        @return:
        '''
        return self.sheet_data.row_values(row)
