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
from public.pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest
import os

class HomeTest(unittest.TestCase):
    '''
        首页的测试用例
    '''

    def save_img(self, img_name):
        """
        ## 为了让BeautifulReport进行自动的失败截图，必须在测试类定义该save_img方法
          传入一个img_name, 并存储到修改后的文件路径下：当前项目的report/mg文件夹，必须存在该文件夹；
        :param img_name: 图片名称，无需后缀
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('/report/img'), img_name))


    global home_url
    global search_input
    global search_button
    global register
    global login

    home_url = 'http://antgoculture.com/index'
    search_input = (By.CSS_SELECTOR, '.input')
    search_button = (By.CSS_SELECTOR, '.search')
    register = (By.CSS_SELECTOR, 'div.text > a:nth-child(1)')
    login = (By.CSS_SELECTOR, 'div.text > a:nth-child(2)')

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @BeautifulReport.add_test_img('test_search_1')
    def test_search_1(self):
        search_content = '1'
        HomePage.search_content(search_input, search_content)
        HomePage.do_search(search_button)
        HomePage.is_page_title(search_content)

    @BeautifulReport.add_test_img('test_search_one')
    def test_search_one(self):
        search_content = 'one'
        HomePage.search_content(search_input,search_content)
        HomePage.do_search(search_button)
        HomePage.is_page_title(search_content)

    @BeautifulReport.add_test_img('test_search_中国')
    def test_search_中国(self):
        search_content = '中国'
        HomePage.search_content(search_input,search_content)
        HomePage.do_search(search_button)
        HomePage.is_page_title(search_content)