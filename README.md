# Selenium_Data_Frame
基于Selenium的数据驱动自动化测试框架_雏形

框架思路是常见的pageobject思路
使用：
  1.先修改config/path.ini里的路径值（绝对路径）
    1.1.test_path：test_case文件夹的路径，放测试用例的，unitest读取该文件夹中符合特征的py类进行测试运行
    1.2.report_path：report文件夹的路径，放html测试报告
  2.在pages中添加xxx_page.py文件
    1.1.其中的函数主要是对应页面的一些操作
  3.在test_case中添加x_test_xxx.py文本（本类继承unitest.Test）【建议复制例子的类然后再修改】
    3.1.第一个x是执行顺序
    3.2.后面的xxx最好是和page类的xxx一致，方便查看
    3.3.其中的函数主要是测试用例
  4.如果要发送邮件，则配置config/email.ini文件
  5.执行run.py
  6.report文件夹下查看报告。如果配置了邮箱，也可以去收件邮箱中查找

ps.BasePage.py中的方法，需要根据项目需求进行补充
