"""
__author__ = 'LZL'
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

from public.common.operation_ini import OperationIni
from public.common.operation_log import OperationLog
import os

class UtilIni():


    def __init__(self):
        self.base_path = os.path.dirname(os.path.realpath(__file__)).split('\\Selenium_Data_Frame')[0]
        self.ini_path = self.base_path + '\\Selenium_Data_Frame\config\config.ini'

    def get_ini_path(self):
        return self.base_path + '\\Selenium_Data_Frame\config\config.ini'

    def get_OperationLog(self):
        log_path = self.base_path+"\\"+OperationIni(self.ini_path).get_value('path', 'log_file_path')
        return OperationLog(log_path)

    def get_case_path(self, case_name='test_case_path'):
        return self.base_path+"\\"+OperationIni(self.ini_path).get_value('path', case_name)

    def get_report_path(self, report_path='report_path'):
        return self.base_path + "\\" + OperationIni(self.ini_path).get_value('path', report_path)

    def get_cookie_path(self, cookie_path = 'cookie_path'):
        return self.base_path + "\\" + OperationIni(self.ini_path).get_value('path', cookie_path)