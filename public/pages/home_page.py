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

from public.pages.base.base_page import BasicPage
from selenium.webdriver.common.by import By

class HomePage(BasicPage):
    '''
    首页，继承BasicPage类
    '''


    def open_url(self, home_url):
        '''
        打开首页并最大化，重写父类方法
        :return:null
        '''
        BasicPage.open_url(home_url)

    def search_content(self, search_input, search_content):
        '''
        定位搜索输入框并输入值
        :param search_input: 元组(By.xxx,输入框元素路径)
        :param search_content: 搜索内容
        :return: null
        '''
        BasicPage.input_value(search_input, search_content, is_clear=True)

    def do_search(self, search_button):
        '''
        定位搜索按键并点击
        :param search_button: 元组(By.xxx,搜索按键元素路径)
        :return: null
        '''
        BasicPage.get_element(search_button).click()

    def to_register(self, register):
        '''
        定位注册并点击跳转
        :param register: 元组(By.xxx,注册按键元素路径)
        :return:
        '''
        BasicPage.get_element(register).click()

    def to_login(self, login):
        '''
        定位注册并点击跳转
        :param login: 元组(By.xxx,注册按键元素路径)
        :return:
        '''
        BasicPage.get_element(login).click()

if __name__ == '__main__':
    page = HomePage()
    page.open_url('http://antgoculture.com/index')









