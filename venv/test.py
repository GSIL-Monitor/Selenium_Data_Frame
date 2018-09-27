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

from selenium import webdriver
import time
from public.pages.base.base_page import BasicPage

phone_css = 'div.input:nth-child(1) > input:nth-child(1)'
password_css = 'div.input:nth-child(3) > input:nth-child(1)'
login_button = ('class name', 'login_btn')
name_value = ('class name', 'name')
name_index = '0'


driver = webdriver.Chrome()
driver.get('http://antgoculture.com/inClassDetails/introduction?id=92')
# driver.maximize_window()
# driver.find_element_by_css_selector(phone_css).send_keys('13710781009')
# driver.find_element_by_css_selector(password_css).send_keys('qwe123')
# driver.find_element('class name', 'login_btn').click()


# BasicPage(driver).save_cookies()
BasicPage(driver).add_cookies()
time.sleep(1)
driver.find_element_by_class_name('btn').click()
# driver.refresh()
# print(driver.get_cookies())
# BasicPage(driver).write_json_file()

# time.sleep(2)
# name = driver.find_elements(name_value[0], name_value[1])[0].text
#
# print(name)


# cookies = driver.get_cookies()
# print(cookies)
# print(driver.get_cookie('PHPSESSID'))
