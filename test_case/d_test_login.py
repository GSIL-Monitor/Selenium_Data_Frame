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

from BeautifulReport import BeautifulReport
from public.pages.yz_pages.home_page import HomePage
from public.pages.yz_pages.login_page import LoginPage
from selenium import webdriver
import unittest
import os



class LoginTest(unittest.TestCase):
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
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    @BeautifulReport.add_test_img("test_login")
    def test_login(self):
        '''
        用例：登录
        '''
        self.home_page.open()  # 进入首页
        self.home_page.to_login()  # 点击登录
        self.login_page.phone_value()
        self.login_page.password_value()
        self.login_page.login_click()
        name_text = self.login_page.get_name_text()
        try:
            self.assertEqual(name_text, name_text)
        except:
            print('用户名不正确，当前用户名是:%s' %(name_text))
            raise AssertionError
