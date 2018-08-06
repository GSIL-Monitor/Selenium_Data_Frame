"""
__author__ = 'LZL'
__mtime__ = '2018/8/6'
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

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasicPage(object):
    ''' 所有页面的基类 '''

    def __init__(self):
        '''
        获得deriver，
        '''
        self.driver = webdriver.Chrome()

    def open_url(self, url):
        '''
        打开指定url并最大化窗口
        :param url: 指定url
        :return:
        '''
        self.driver.get(url)
        self.driver.maximize_window()

    def get_element(self, args):
        '''
        定位元素，显示等待10秒
        :param args: 元组（By.xx,元素路径）
        :return: 元素对象
        '''
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(args))
        return self.driver.find_element(args[0], args[1])


    def do_js(self, js):
        '''
        执行js
        :param js: 要执行的js
        :return: null
        '''
        self.driver.execute_script(js)


    def input_value(self, args, value, is_clear=True):
        '''
        输入框输入关键字
        :param args: 要定位的元素元组（By.xxx, 元素路径）
        :param value: 关键字
        :param is_clear: 是否先清空输入框
        :return: null
        '''
        input = self.get_element(args)
        if is_clear:
            input.clear()
        input.send_keys(value)

    def is_pagetitle(self, pagetitle):
        '''
        判断页面标题是否包含某字段
        @param pagetitile: 需判断的字段
        @return: True/False
        '''
        return pagetitle in self.driver.title

    def is_current_url(self, current_url):
        '''
              判断url是否包含某字段
              @param current_url: 需判断的url字段
              @return: True/False
        '''
        return current_url in self.driver.current_url
















