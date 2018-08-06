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
import logging

class OperationLog(object):
    '''
    对日志文件的操作类（生成的html测试报告中有错误记录和截图，所以不调用该类了）
    '''

    def __init__(self, log_path, log_level=logging.ERROR):
        '''
        获得指定log文件对象以及设置该log文件的内容组成
        :param log_path: log文件路径
        :param log_level: 记录的级别
        '''
        logging.basicConfig(
            filename=log_path,  # log文件路径
            filemode='a+',  # 追加模式
            level=log_level,  # 日志级别
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(linename)s %(message)s',  # 内容格式
            datefmt='%Y:%m:%d %H%M%S',  # 内容的时间格式
        )

    def debug(self, message):
        '''
        设置日志的DEBUG级别的内容
        @param message: 内容
        @return: null
        '''
        logging.debug(message)

    def info(self, message):
        '''
        设置日志的INFO级别的内容
        @param message: 内容
        @return: null
        '''
        logging.info(message)


    def warn(self, message):
        '''
        设置日志的WAR级别的内容
        @param message: 内容
        @return: null
        '''
        logging.warning(message)

    def error(self, message):
        '''
        设置日志的ERROR级别的内容
        @param message: 内容
        @return: null
        '''
        logging.error(message)


    def cri(self, message):
        '''
        设置日志的critical级别的内容
        @param message: 内容
        @return: null
        '''
        logging.critical(message)
