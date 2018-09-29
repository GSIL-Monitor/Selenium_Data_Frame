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

from public.pages.base.base_page import BasicPage
from public.util.util_ini import UtilIni
import logging
from selenium.webdriver.common.by import By
import time

class HomePage(BasicPage):
    '''
    首页，继承BasicPage类
    '''

    UtilIni().get_OperationLog()
    home_url = 'http://antgoculture.com/index'
    search_input = (By.CSS_SELECTOR, '.input')
    search_button = (By.CSS_SELECTOR, '.search')
    register = (By.CSS_SELECTOR, 'div.text > a:nth-child(2)')
    login = (By.CSS_SELECTOR, 'div.text > a:nth-child(1)')
    # page_title = '新蚁族'


    def open(self):
        '''
        打开首页并最大化，重写父类方法
        ps.方法名不能和父类一样，否则下面的self.xxx就会引用当前类的方法
        :return:null
        '''
        self.open_url(self.home_url)

    def search_content(self, search_content):
        '''
        定位搜索输入框并输入值
        :param search_content: 搜索内容
        :return: null
        '''
        self.input_content(self.search_input, content=search_content, is_clear=True)

    def do_search(self):
        '''
        定位搜索按键并点击
        :return: null
        '''
        self.get_element(self.search_button).click()

    def to_register(self):
        '''
        定位注册并点击跳转
        :return:
        '''
        self.get_element(self.register).click()

    def to_login(self):
        '''
        定位登录并点击跳转
        :return:
        '''
        try:
            self.get_element(self.login).click()
        except:
            logging.warning('首页登录按键点击失败')
            print('首页登录按键点击失败')

    def is_success(self, page_title):
        '''
        根据页面的title判断是否处于当前页面，调用父类方法
        :return:True/False
        '''
        return self.is_page_title(page_title)










