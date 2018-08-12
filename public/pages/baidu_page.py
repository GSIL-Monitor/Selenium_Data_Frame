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

    def open(self, url):
        self.open_url(url)

    def search(self, args, content):
        self.input_content(args, content)

    def click(self, args):
        self.get_element(args).click()

    def is_success(self, content):
        self.is_page_title(content)
