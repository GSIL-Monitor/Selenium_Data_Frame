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

# 导入smtplib发送邮件模块，发送和接收都是由smtplib.SMTP方法来完成的
import smtplib
# 组装邮件的内容
from email.mime.multipart import MIMEMultipart
# 主要用于完善邮箱内容和标题的定义
from email.mime.text import MIMEText
from email.header import Header

import os
# 通过ini文件获取发送邮件所需的参数值
from public.common.operation_ini import OperationIni

class SendMail:
    ''' 发送带有附件的邮件 '''

    def get_email_obj(self, email_sub, email_from, email_to_list):
        '''
        构建邮件对象，设置邮件主题、发件人、收件人
        @param email_sub:  邮件主题
        @param email_from:  发件人昵称
        @param email_to_list: 收件人list
        @return: 邮件对象
        '''

        # 创建根容器
        email_obj = MIMEMultipart('related')
        # 邮件主题、发件人、收件人
        email_obj['Subject'] = Header(email_sub, 'utf-8')
        # 以,号连接收件人地址
        email_to = ','.join(email_to_list)
        email_obj['From'] = Header(email_from)
        email_obj['To'] = Header(email_to)
        return email_obj

    def attach_content(self, email_obj, email_content='', content_type='plain', charset='utf-8'):
        '''
        创建邮件正文，并附加到根容器中。
        @param email_obj:  邮件对象，根容器
        @param email_content:  邮件正文
        @param content_type: 邮件内容格式，默认纯文本plain；可以是html
        @param charset: 编码格式，默认utf-8
        @return: null
        '''
        # 创建邮箱正文
        content = MIMEText(email_content, content_type, charset)
        # 将邮件正文附加到根容器
        email_obj.attach(content)

    def attach_adjunct(self, email_obj, adjunct_path, adjunct_name):
        '''
        添加附件到根容器，可以是文件也可以是文档
        @param email_obj: 邮件对象：根容器
        @param adjunct_path:  附件文件的路径
        @param adjunct_name:  附件名称
        @return: null
        '''

        # 创建附件对象并将附件添加到附件对象上；'octet-stream': binary data
        adjunct = MIMEText(open(adjunct_path, 'rb').read(), 'base64', 'utf-8')

        adjunct["Content-Type"] = 'application/octet-stream'
        # 给附件添加头文件、设置名称，带格式
        adjunct["Content-Disposition"] = 'attachment; filename="%s"'%adjunct_name
        # 附件添加到根容器中
        email_obj.attach(adjunct)

    def send_mail(self, email_obj, email_host, host_port, email_from, email_pwd, email_to_list):
        '''
        发送邮件
        @param email_obj: 邮件对象
        @param email_host: SMTP服务器主机
        @param host_port: SMTP服务端口号
        @param email_from: 发件地址
        @param email_pwd: 发送地址的授权码，不是密码
        @param email_to_list: 收件地址：list
        @return: True：成功；False：失败
        '''
        try:
            # 连接smtp邮箱服务器
            smtp_obj = smtplib.SMTP_SSL(email_host, host_port)
            # 登陆发件邮箱：邮箱和对应授权码
            smtp_obj.login(email_from, email_pwd)
            smtp_obj.sendmail(email_from, email_to_list, email_obj.as_string())
            smtp_obj.quit()
            print('发送成功')
            return True
        except smtplib.SMTPException:
            print('发送失败')
            return False

    def get_new_report(self, report_path):
        '''
            返回指定目录下的最新文件的绝对路径
        @param report_path: 附件所处的目录
        @return: 该目录下最新文件的绝对路径
        '''

        # 列出该目录下的文件夹和文件，数组的形式
        reports = os.listdir(report_path)
        # 对该目录的文件进行排序，并获取最新的一个文件
        ## list.sort(key = lambda xx : xxxx)，自定义排序方式，lambda是匿名函数
        reports.sort(key=lambda report: os.path.getmtime(report_path + '\\' + report))
        new_report = os.path.join(report_path + '\\' + reports[-1])
        return new_report

    def __send_config(self):
        '''
        读取email.ini文件中的邮件属性值发送邮件
        附件为report文件夹下最新的文件
        若有想更改的，直接更改ini文件
        :return: null
        '''

        # base_path = os.path.dirname(os.path.realpath(__file__))
        # 拼接路径，读取ini文件中发送邮件所需要的参数值
        base_path = os.path.dirname(os.getcwd()).split('\\public')[0]
        ini_path = os.path.join(base_path, 'parameter', 'email.ini')
        report_path = os.path.join(base_path, 'report', 'html')

        ini = OperationIni(ini_path)
        email_host = ini.get_value('server', 'email_host')
        host_port = ini.get_value('server', 'host_port')
        from_addr = ini.get_value('server', 'from_Addr')
        pwd = ini.get_value('server', 'pwd')
        email_from = ini.get_value('content', 'email_from')
        to_addr_list = ini.get_value('content', 'to_addr_list')
        email_content = ini.get_value('content', 'email_content')
        email_subject = ini.get_value('content', 'email_subject')
        part_name = ini.get_value('content', 'part_name')
        # report文件夹下最新的一个文件为附件
        Email = SendMail()
        adjunct_path = Email.get_new_report(report_path)

        # 调用本类方法，发送邮件
        email_obj = Email.get_email_obj(email_subject, email_from, to_addr_list)
        #  正文若是文本则不需要传参content_type
        Email.attach_content(email_obj, email_content)
        Email.attach_adjunct(email_obj, adjunct_path, part_name)
        print(to_addr_list, type(to_addr_list))
        Email.send_mail(email_obj, email_host, host_port, from_addr, pwd, to_addr_list.split(','))


    def send_email(self):
        '''
        调用私有方法进行邮件发送，可更改email.ini文件进行相关修改
        :return: null
        '''
        self.__send_config()


if __name__ == "__main__":
    SendMail().send_email()


