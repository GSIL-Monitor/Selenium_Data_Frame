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
from public.pages.yz_pages.micro_page import MicroPage
from public.pages.yz_pages.login_page import LoginPage
from selenium import webdriver
import unittest
import os

class MicroTest(unittest.TestCase):

    '''
    用例：购买/学习微课程
    '''

    phone = '13710781009'
    password = 'qwe123'

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
        cls.mirco_page = MicroPage(cls.driver)
        UtilIni().get_OperationLog()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    @BeautifulReport.add_test_img("test_micro")
    def test_micro(self):
        # 登录
        self.home_page.open()
        self.home_page.to_login()
        self.login_page.phone_value(self.phone)
        self.login_page.password_value(self.password)
        self.login_page.login_click()

        self.mirco_page.to_micro()  # 点击微课程
        self.mirco_page.click_free()  # 点击免费筛选
        self.mirco_page.to_detail()  # 进入最后的一个课程详情页






