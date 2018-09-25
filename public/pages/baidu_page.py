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

class Baidu_Page(BasicPage):

    url = 'http://www.baidu.com'
    search_ele = ("id", 'kw')
    button_ele = ("id", 'su')

    def open(self):
        self.open_url(self.url)

    def search(self, content):
        self.input_content(self.search_ele, content)

    def click(self):
        self.get_element(self.button_ele).click()

    def is_success(self, content):
        self.is_page_title(content)
