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

from configparser import ConfigParser

class OperationIni(object):
    ''' 读取ini文件内容 '''

    def __init__(self, ini_path):
        '''
        获取ini文件对象
        @param ini_path: ini文件绝对路径
        '''
        self.cp = ConfigParser()
        # ini文件中若有中文，则会自动转成gbk，读取会读取不了或乱码，所以这里需要注意设置编码
        self.cp.read(ini_path, encoding="utf-8")
        # self.cp.read(ini_path, encoding="utf-8-sig")

    def get_sections(self):
        '''
        获得所有sections
        @return: 列表形式返回ini文件中所有的节
        '''
        return self.cp.sections()

    def get_options(self, section):
        '''
        获得指定节的所有参数中的键
        @param section:节名
        @return:列表形式返回指定节的所有参数键值对中的键
        '''
        return self.cp.options(section)

    def get_items(self, section):
        '''
         获得指定节的所有参数key-value
        @param section: 节名
        @return: 列表形式返回获得指定节的所有参数key-value,其中key-value是元组形式
        '''
        return self.cp.items(section)

    def get_value(self, section, option):
        '''
        获取指定节中指定参数中的value
        @param section: 节名
        @param option: 参数key
        @return: 参数value，返回string
        '''
        return self.cp.get(section, option)