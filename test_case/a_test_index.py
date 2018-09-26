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

class SearchTest(unittest.TestCase):
    '''
        搜索的测试用例
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
        cls.homepage = HomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    @BeautifulReport.add_test_img('test_to_index')
    def test_to_index(self):
        self.homepage.open()
        try:
            self.homepage.is_success()
        except AssertionError:
            logging.warning('进入首页失败')
            raise AssertionError



if __name__ == '__main__':
    unittest.main()