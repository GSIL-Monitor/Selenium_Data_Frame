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

import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasicPage():
    ''' 所有页面的基类 '''

    def __init__(self, driver):
        '''
        获得deriver，
        '''
        self.driver = driver

    def open_url(self, url):
        '''
        打开指定url并最大化窗口
        :param url: 指定url
        :return:
        '''
        self.driver.get(url)
        self.driver.maximize_window()

    def get_element(self, locator):
        '''
        定位元素，显性等待10秒
        :param locator: 元组（By.xx,元素路径）
        :return: 元素对象
        '''
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(locator[0], locator[1])
        except:
            print('使用%s定位的%s元素定位失败'%(locator[0], locator[1]))

    def do_js(self, js):
        '''
        执行js
        :param js: 要执行的js
        :return: null
        '''
        self.driver.execute_script(js)

    def input_content(self, locator, content, is_clear=True):
        '''
        输入框输入关键字
        :param locator: 要定位的元素元组（By.xxx, 元素路径）
        :param content: 关键字
        :param is_clear: 是否先清空输入框
        :return: null
        '''
        input = self.get_element(locator)
        if is_clear:
            input.clear()
        input.send_keys(content)

    def is_page_title(self, pagetitle):
        '''
        判断页面标题是否包含某字段
        @param pagetitile: 需判断的字段
        @return: True/False
        '''
        # return self.assertIn(pagetitle, self.driver.title)
        return WebDriverWait(self.driver, 10).until(EC.title_contains(pagetitle))

    def is_current_url(self, current_url):
        '''
              判断url是否包含某字段
              @param current_url: 需判断的url字段
              @return: True/False
        '''
        return self.assertIn(current_url, self.driver.current_url)


    def is_visibility(self, locator):
        '''
        元素的属性是否可见
        :param locator: 元组（By.xx,元素路径）
        :return: True/False
        '''
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))


    def move_to_element(self, locator):
        '''
        鼠标移动到指定的元素上方
        :param locator: 元组（By.xx,元素路径）
        :return: None
        '''
        element = self.get_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def forward(self):
        '''
        前进一页
        :return:None
        '''
        self.driver.forward()

    def back(self):
        '''
        后退一页
        :return:None
        '''
        self.driver.back()

    def open_at_current(self, locator, js):
        '''
        执行让target属性值变空的js，并点击该元素
        :param locator:
        :param js: target属性值变空；例如：document.getElementsByClassName("mnav")[0].target="";
        :return: None
        '''
        self.do_js(js)
        self.get_element(locator).click()

