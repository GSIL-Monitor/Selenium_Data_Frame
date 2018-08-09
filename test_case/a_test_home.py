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
import time

class HomeTest(unittest.TestCase):
    '''
        首页的测试用例
    '''

    def save_img(self, img_name):
        """
        ## 为了让BeautifulReport进行自动的失败截图，必须在测试类定义该save_img方法
          传入一个img_name, 并存储到默认的图片保存路径：当前项目的img文件夹，必须存在该文件夹；
        :param img_name: 图片名称，无需后缀
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath('img'), img_name))

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.home_url = 'http://xxx.com/index'
        cls.search_input = (By.CSS_SELECTOR, '.input')
        cls.search_button = (By.CSS_SELECTOR, '.search')
        cls.register = (By.CSS_SELECTOR, 'div.text > a:nth-child(1)')
        cls.login = (By.CSS_SELECTOR, 'div.text > a:nth-child(2)')

    @BeautifulReport.add_test_img('test_1')
    def test_1(self):
        search_content = '1'
        # 注意要初始化HomePage对象
        homepage = HomePage(self.driver)
        homepage.open(self.home_url)
        homepage.search_content(self.search_input, search_content)
        homepage.do_search(self.search_button)
        # 这里延迟1s进行判断，因为从首页进来搜索时，title的更新会慢一点
        time.sleep(1)
        homepage.is_success(search_content)

    @BeautifulReport.add_test_img('test_2')
    def test_2(self):
        search_content = 'one'
        homepage = HomePage(self.driver)
        homepage.open(self.home_url)
        homepage.search_content(self.search_input, search_content)
        homepage.do_search(self.search_button)
        homepage.is_success(search_content)

    @BeautifulReport.add_test_img('test_3')
    def test_3(self):
        search_content = '中国'
        homepage = HomePage(self.driver)
        homepage.open(self.home_url)
        homepage.search_content(self.search_input, search_content)
        homepage.do_search(self.search_button)
        homepage.is_success(search_content)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

# if __name__ == '__main__':
#     unittest.main()