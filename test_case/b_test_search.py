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

from public.pages.yz_pages.home_page import HomePage
from BeautifulReport import BeautifulReport
from public.util.util_ini import UtilIni
from selenium import webdriver
import unittest
import logging
import os

class SearchTest(unittest.TestCase):
    '''
        用例：搜索功能
    '''

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
        UtilIni().get_OperationLog()

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
            self.homepage.is_success(search_content)
        except AssertionError:
            logging.warning('纯数字搜索，结果对比错误')
            raise AssertionError


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
            self.homepage.is_success(search_content)
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
            self.homepage.is_success(search_content)
        except AssertionError:
            logging.warning('纯中文搜索，结果对比错误')
            raise AssertionError

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
