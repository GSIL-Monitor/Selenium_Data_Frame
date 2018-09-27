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

class MicroPage(BasicPage):

    UtilIni().get_OperationLog()
    micro_css = 'html body div#app div header.header_box div.header.clear nav.fl ul.header_menu.clear li a'
    free_css = 'html body div#app div section.inClass_con_box div.con ul.inClass_option_con li.clear ul.list.fr.clear li a'
    class_locator = ('class name', 'clear')
    class_index = -1
    money_css = '.money > span:nth-child(1)'
    study_locator = ('class name', 'btn')
    current_url = 'video'

    def to_micro(self):
        self.get_element_by_css(self.micro_css).click()

    def click_free(self):
        self.get_element_by_css(self.free_css).click()

    def to_detail(self):
        return self.get_elements(self.class_locator, self.class_index).click()

    def get_money_value(self):
        return self.get_element_by_css(self.money_css)

    def click_study(self):
        self.get_element(self.study_locator).click()

    def get_btn_text(self):
        self.get_element(self.study_locator).text

    def in_video(self):
        self.is_current_url(self.current_url)
