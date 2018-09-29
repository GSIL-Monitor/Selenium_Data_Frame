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
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time


class MicroPage(BasicPage):
    UtilIni().get_OperationLog()
    micro_css = '.header_menu > li:nth-child(2) > a:nth-child(1)'
    free_css = 'li.clear:nth-child(2) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)'
    free_class_css = 'li.clear:nth-child(2) > ul:nth-child(2) > li:nth-child(2)'
    class_css = '.class_list_box > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)'
    money_css = '.money > span:nth-child(1)'
    study_locator = ('class name', 'btn')
    current_url = 'video'

    def to_micro(self):
        try:
            self.get_element_by_css(self.micro_css).click()
        except:  # 这个步骤会出现这个错误，刷新重新定位
            self.get_element_by_css(self.micro_css).click()

    def click_free(self):
        time.sleep(2)
        self.get_element_by_css(self.free_css).click()

    def to_detail(self):
        time.sleep(2)  #　使用了显示等待，但是还是会出错，没办法只能这样了
        return self.get_element_by_css(self.class_css).click()

    def get_money_value(self):
        time.sleep(2)  #　使用了显示等待，但是还是会出错，没办法只能这样了
        return self.get_element_by_css(self.money_css).text

    def click_study(self):
        self.get_element(self.study_locator).click()

    def get_btn_text(self):
        return self.get_element(self.study_locator).text

    def in_video(self):
        time.sleep(2)  #　这里用不了显示等待，只能这样了。。
        return self.is_current_url(self.current_url)
