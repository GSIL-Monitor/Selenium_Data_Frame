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

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from public.util.util_ini import UtilIni
import logging
import json
import operator as op

class BasicPage():
    ''' 所有页面的基类 '''

    ini = UtilIni()
    ini.get_OperationLog()

    def __init__(self, driver):
        '''
        获得deriver
        '''
        try:
            self.driver = driver
        except:
            logging.warning('获取driver失败' )
            print('获取driver失败')
            raise Exception

    def open_url(self, url):
        '''
        打开指定url并最大化窗口
        :param url: 指定url
        :return:
        '''
        try:
            self.driver.get(url)
            self.driver.maximize_window()
        except:
            logging.warning('打开%s失败'%(url))
            print('打开%s失败'%(url))
            raise Exception

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
            logging.warning('使用%s定位的%s元素定位失败'%(locator[0], locator[1]))
            print('使用%s定位的%s元素定位失败'%(locator[0], locator[1]))
            raise Exception

    def get_element_by_css(self, css):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_css_selector(css))
            return self.driver.find_element_by_css_selector(css)
        except:
            logging.warning('css定位失败，css语句是：%s'%(css))
            print('css定位失败，css语句是：%s'%(css))
            raise Exception

    def get_elements(self, locator, index):
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(locator[0], locator[1])[index])
            return self.driver.find_elements(locator[0], locator[1])[index]
        except:
            logging.warning('使用%s定位的%s中的第%s个元素定位失败' % (locator[0], locator[1], index))
            print('使用%s定位的%s中的第%s个元素定位失败' % (locator[0], locator[1], index))
            raise Exception

    def do_js(self, js):
        '''
        执行js
        :param js: 要执行的js
        :return: null
        '''
        try:
            self.driver.execute_script(js)
        except:
            logging.warning('使用js语句定位失败：%s' % (js))
            print('使用js语句定位失败：%s' % (js))


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
        return WebDriverWait(self.driver, 10).until(EC.title_contains(pagetitle))


    def is_current_url(self, current_url):
        '''
              判断url是否包含某字段
              @param current_url: 需判断的url字段
              @return: True/False
        '''
        return op.contains(current_url, self.driver.current_url)


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
        让新打开窗口的超链在当前窗口打开；执行让target属性值变空的js，并点击该元素
        :param locator:
        :param js: target属性值变空；例如：document.getElementsByClassName("mnav")[0].target="";
        :return: None
        '''
        self.do_js(js)
        self.get_element(locator).click()


    def get_attribute(self, locator, ab_name):
        '''
        获取元素的属性
        :param locator:
        :param ab_name:
        :return:
        '''
        element = self.get_element(locator)
        return element.get_attribute(ab_name)


    def focus_to_element(self, locator):
        '''
        聚焦到元素位置（跳到）
        :param locator:
        :return:
        '''
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def scroll_top(self):
        '''
        滚动到顶部
        :return:
        '''
        js = 'window.scrollTo(0,0)'
        self.do_js(js)


    def scroll_end(self):
        '''
        滚动到底部
        :return:
        '''
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.do_js(js)


    def select_by_index(self, locator, index):
        '''
        通过索引定位下拉框的值
        :param locator:
        :param index:
        :return:
        '''
        element = self.get_element(locator)
        Select(element).select_by_index(index)


    def select_by_value(self, locator, value):
        '''
        通过value定位下拉框的值
        :param locator:
        :param value:
        :return:
        '''
        element = self.get_element(locator)
        Select(element).select_by_value(value)


    def select_by_text(self, locator, text):
        '''
        通过text定位下拉框的值
        :param locator:
        :param value:
        :return:
        '''
        element = self.get_element(locator)
        Select(element).select_by_visible_text(text)

    def save_cookies(self):
        cookies_list = self.driver.get_cookies()
        cookie_path = self.ini.get_cookie_path()
        with open(cookie_path, 'w', encoding='utf-8') as f:
            json.dump(cookies_list, f)

    def add_cookies(self):
        cookie_path = self.ini.get_cookie_path()
        with open(cookie_path) as f:
            cookies_list = json.load(f)
            self.driver.delete_all_cookies()
            for cookie in cookies_list:
                self.driver.add_cookie(
                {
                    'domain': '.xxxx.com',  # 此处xxx.com前，需要带点
                    'name': cookie['name'],
                    'value': cookie['value'],
                    'path': '/',
                    'expires': None
                }
                )
            print(self.driver.get_cookies())

