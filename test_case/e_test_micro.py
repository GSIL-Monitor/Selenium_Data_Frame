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
        cls.micro_page = MicroPage(cls.driver)
        UtilIni().get_OperationLog()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @BeautifulReport.add_test_img("test_micro")
    def test_micro(self):
        '''
        用例：免费课程学习
        :return:
        '''
        # 登录
        self.home_page.open()
        self.home_page.to_login()
        self.login_page.phone_value()
        self.login_page.password_value()
        self.login_page.login_click()

        self.micro_page.to_micro()  # 点击微课程
        self.micro_page.click_free()  # 点击免费筛选
        self.micro_page.to_detail()  # 进入第一个课程详情页
        money = self.micro_page.get_money_value()
        print('money =>', money)
        self.assertEqual("免费", money)  # 判断进入的课程是否是免费课程

        btn_text = self.micro_page.get_btn_text()  # 获取该课程的按钮的文本
        if btn_text == '立即购买':  # 进行购买
            self.micro_page.click_study()
            self.assertEqual(self.micro_page.get_btn_text(), "立即学习")  # 文本会改变
        else:
            self.micro_page.click_study()  # 点击进入学习
            self.assertTrue(self.micro_page.in_video())  # url包含video
