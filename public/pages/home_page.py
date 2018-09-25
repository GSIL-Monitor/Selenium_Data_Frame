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
from selenium.webdriver.common.by import By

class HomePage(BasicPage):
    '''
    首页，继承BasicPage类
    '''

    home_url = 'http://antgoculture.com/index'
    search_input = (By.CSS_SELECTOR, '.input')
    search_button = (By.CSS_SELECTOR, '.search')
    register = (By.CSS_SELECTOR, 'div.text > a:nth-child(1)')
    login = (By.CSS_SELECTOR, 'div.text > a:nth-child(2)')

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
        :param search_input: 元组(By.xxx,输入框元素路径)
        :param search_content: 搜索内容
        :return: null
        '''
        self.input_content(self.search_input, content=search_content, is_clear=True)

    def do_search(self):
        '''
        定位搜索按键并点击
        :param search_button: 元组(By.xxx,搜索按键元素路径)
        :return: null
        '''
        self.get_element(self.search_button).click()

    def to_register(self):
        '''
        定位注册并点击跳转
        :param register: 元组(By.xxx,注册按键元素路径)
        :return:
        '''
        self.get_element(self.register).click()

    def to_login(self,):
        '''
        定位注册并点击跳转
        :param login: 元组(By.xxx,注册按键元素路径)
        :return:
        '''
        self.get_element(self.login).click()

    def is_success(self, pagetitle):
        '''
        根据页面的title判断是否处于当前页面，调用父类方法
        :param pagetitle: 判断关键字，包含
        :return:True/False
        '''
        return self.is_page_title(pagetitle)










