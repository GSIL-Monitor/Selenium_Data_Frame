from BeautifulReport import BeautifulReport
from public.pages.baidu_page import Baidu_Page
from selenium.webdriver.common.by import By
from public.common.operation_log import OperationLog
from selenium import webdriver
import logging
import unittest
import time
import os


class BaiduTest(unittest.TestCase):
    global log_path
    # 如果是处于根目录下的py文件调用本类，则使用这个
    base_path = os.path.dirname(os.path.realpath(__file__)).split('\\test_case')[0]
    # 如果是处于根目录下的第一层级目录调用本类，则使用这个
    # base_path = os.path.dirname(os.getcwd()).split('\\test_case')[0]

    time = time.strftime('%m.%d', time.localtime())
    log_path = os.path.join(base_path, 'log', '%s.log' % (time))

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
        cls.url = 'http://www.baidu.com'
        cls.page = Baidu_Page(cls.driver)
        cls.search_ele = (By.ID, 'kw')
        cls.button_ele = (By.ID, 'su')
        cls.log = OperationLog(log_path, logging.WARN)

    @BeautifulReport.add_test_img('test_baidu_one')
    def test_baidu_one(self):
        '''
        纯数字搜索；sleep再判断
        '''
        content = '123'
        self.page.open(self.url)
        self.page.search(self.search_ele, content)
        self.page.click(self.button_ele)
        try:
            self.page.is_success(content)
        except AssertionError:
            logging.warning('纯数字搜索，结果对比错误')
            raise AssertionError


    @BeautifulReport.add_test_img('test_baidu_two')
    def test_baidu_two(self):
        '''
        纯中文搜索，不sleep判断
        '''
        content = '海贼王'
        self.page.open(self.url)
        self.page.search(self.search_ele, content)
        self.page.click(self.button_ele)
        try:
            self.page.is_success(content)
        except AssertionError:
            logging.warning('纯中文搜索，结果对比错误')
            raise AssertionError

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


# if __name__ == '__main__':
#     unittest.main()