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
from public.common.send_mail import SendMail
import unittest
import os
import time

class Run(object):
    '''
    执行测试类，生成测试报告并发送邮件
    '''



    def add_test_case(self, test_path, py_rule='*test*.py'):
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

    def begin_run(self,test_path, report_path, report_name):
        test_suite = self.add_test_case(test_path)
        self.do_report(test_suite, save_path=report_path, report_name=report_name)
        SendMail().send_email()


if __name__ == '__main__':
    # 项目路径
    base_path = os.path.dirname(os.path.realpath(__file__))
    # TestCase路径
    test_path = os.path.join(base_path, 'test_case')
    # html测试报告路径
    report_path = os.path.join(base_path, 'report', 'html')
    # 测试报告名称
    time = time.strftime('%m.%d', time.localtime())
    report_name = ''.join([time, '执行的测试报告'])
    run = Run()
    run.begin_run(test_path=test_path, report_path=report_path, report_name=report_name)
