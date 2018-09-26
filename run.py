"""
__author__ = 'LZL'
__mtime__ = '2018/8/8'
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

from BeautifulReport import BeautifulReport
from public.common.operation_mail import SendMail
from public.common.operation_ini import OperationIni
import unittest
import os
import time

class Run(object):
    '''
    执行测试类，生成测试报告并发送邮件
    '''



    def add_test_case(self, test_path, py_rule):
        '''
        加载所有测试用例
        @param test_path: 测试用例所在目录
        @param py_rule: 测试py文件的正则
        @return: 加载了测试用例的测试套件
        '''
        return unittest.defaultTestLoader.discover(start_dir=test_path, pattern=py_rule)


    def do_report(self, test_suite, save_path, report_name='测试报告', description='自动化测试报告'):
        '''
        运行测试套件，生成测试报告
        @param test_suite: 测试套件
        @param report_name: 测试报告名称，可带html可不带
        @param description: 测试报告注释
        @param save_path: 测试报告保存路径
        @return: null
        '''
        report = BeautifulReport(test_suite)
        report.report(filename=report_name, description=description, log_path=save_path)

    def begin_run(self,test_path, report_path, report_name, py_rule='test*.py'):
        '''
        运行测试用例，生成测试报告，发送邮件
        :param test_path: 测试用例的py文件所在路径
        :param report_path: 测试报告文件保存的路径
        :param report_name: 测试报告的名称
        :param py_rule: 需要加载到测试套件中的测试用例的py文件名称的正则
        :return:
        '''
        test_suite = self.add_test_case(test_path, py_rule)
        self.do_report(test_suite, save_path=report_path, report_name=report_name)
        # SendMail().send_email()


if __name__ == '__main__':

    # 项目路径
    base_path = os.path.dirname(os.path.realpath(__file__))
    # 测试报告名称
    time = time.strftime('%m.%d', time.localtime())
    report_name = ''.join([time, '执行的测试报告'])

    # 读取ini文件中的路径值
    ini_path = os.path.join(base_path, 'config', 'path.ini')
    ini = OperationIni(ini_path)
    test_path = ini.get_value('path', 'test_path')
    report_path = ini.get_value('path', 'report_path')
    run = Run()
    run.begin_run(test_path=test_path, report_path=report_path, report_name=report_name, py_rule='*_test*.py')