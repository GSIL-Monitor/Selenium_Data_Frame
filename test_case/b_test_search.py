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
from public.common.operation_log import OperationLog
import logging
from BeautifulReport import BeautifulReport
from public.pages.yz_pages.home_page import HomePage
from selenium import webdriver
import unittest
import os
import time

class HomeTest(unittest.TestCase):
    '''
        首页的测试用例
    '''

    global log_path
    # 如果是处于根目录下的py文件调用本类，则使用这个
    base_path = os.path.dirname(os.path.realpath(__file__)).split('\\test_case')[0]
    # 如果是处于根目录下的第一层级目录调用本类，则使用这个
    # base_path = os.path.dirname(os.getcwd()).split('\\test_case')[0]

    time = time.strftime('%m.%d', time.localtime())
    log_path = os.path.join(base_path, 'log', '%s.log'%(time))
    OperationLog(log_path, log_level=logging.WARN)



    def save_img(self, img_name):
        """
        ## 为了让BeautifulReport进行自动的失败截图，必须在测试类定义该save_img方法
          传入一个img_name, 并存储到默认的图片保存路径：当前项目的img文件夹，必须存在该文件夹；
        :param img_name: 图片名称，无需后缀
        :return:null
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('img'), img_name))

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 注意要初始化HomePage对象
        cls.homepage = HomePage(cls.driver)


    # BeautifulReport的装饰器，失败截图、保存、添加到报告中；图片名称需和方法名一致
    @BeautifulReport.add_test_img('test_1')
    def test_1(self):
        '''
         纯数字搜索
        '''
        search_content = '1'
        self.homepage.open()
        self.homepage.search_content(search_content)
        self.homepage.do_search()
        try:
            self.homepage.is_success()
        except AssertionError:
            logging.warning('纯数字搜索，结果对比错误')
            # 记得要抛出该异常，否则就算case失败了，也会pass
            raise AssertionError
            # raise后面的代码不会执行了

    @BeautifulReport.add_test_img('test_2')
    def test_2(self):
        '''
        纯英文搜索
        '''
        search_content = 'one'
        self.homepage.open()
        self.homepage.search_content(search_content)
        self.homepage.do_search()
        try:
            self.homepage.is_success()
        except AssertionError:
            logging.warning('纯英文搜索，结果对比错误')
            raise AssertionError

    @BeautifulReport.add_test_img('test_3')
    def test_3(self):
        '''
        纯中文搜索
        '''
        search_content = '中国'
        self.homepage.open()
        self.homepage.search_content(search_content)
        self.homepage.do_search()
        try:
            self.homepage.is_success()
        except AssertionError:
            logging.warning('纯中文搜索，结果对比错误')
            raise AssertionError

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()