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

class LoginPage(BasicPage):


    UtilIni().get_OperationLog()
    phone_css = 'div.input:nth-child(1) > input:nth-child(1)'
    password_css = 'div.input:nth-child(3) > input:nth-child(1)'
    login_button = ('class name', 'login_btn')
    name_value = ('class name', 'name')
    name_index = 0

    def phone_value(self, value):
        try:
            self.get_element_by_css(self.phone_css).send_keys(value)
        except Exception:
            logging.warning('%s元素输入值失败' %(self.phone_css))
            raise Exception

    def password_value(self, value):
        try:
            self.get_element_by_css(self.password_css).send_keys(value)
        except Exception:
            logging.warning('%s元素输入值失败' %(self.password_css))
            raise Exception

    def login_click(self):
        try:
            self.get_element(self.login_button).click()
        except Exception:
            logging.warning('%s点击失败' %(self.login_button[1]))
            raise Exception

    def get_name_text(self):
        return self.get_elements(self.login_button, self.name_index).text

