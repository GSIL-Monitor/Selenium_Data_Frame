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
from public.util.util_ini import UtilIni
from BeautifulReport import BeautifulReport
from public.pages.yz_pages.home_page import HomePage
from selenium import webdriver
import logging
import unittest
import os

class IndexTest(unittest.TestCase):
    '''
        搜索的测试用例
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

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @BeautifulReport.add_test_img('test_to_index')
    def test_to_index(self):
        '''
        用例：进入首页
        :return:
        '''
        search_content = '新蚁族'
        self.homepage.open()
        try:
            self.homepage.is_success(search_content)
            logging.warning('进入首页')
        except AssertionError:
            logging.warning('进入首页失败')
            raise AssertionError



if __name__ == '__main__':
    unittest.main()