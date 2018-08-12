# Selenium_Data_Frame
基于Selenium的数据驱动自动化测试框架_雏形

'''

构造：
  |-- config：ini配置文件的目录
    |-- email.ini 发送邮件需要的配置
    |-- path.ini 测试用例路径、测试报告路径等

  |-- data：测试用例/excel （UI的自动化好像没必要，比直接修改代码更浪费时间）
    |-- xxx.xls

  |-- img：测试报告失败截图的图片的保存目录
    |-- xxx.png

  |-- log：日志的保存目录
    |-- xxx.log

  |-- public 公共类库
    |-- common 公共方法类库
      |-- operation_excel.py 操作excel的类，UI自动化好像没必要了
      |-- operation_ini.py 读取ini文件的类，封装configparser
      |-- operation_log.py 生成log文件的类，封装logging
      |-- operation_mail.py 发送email的类
    |-- pages 各个page的类
      |-- base 基础page类
        |-- base_page.py 基础page的类，二次封装webdriver的一些方法，以及测试页面的公共方法和属性，随时扩充
      |-- xxx_page.py 测试页面的类，基础base_page.py类；封装页面上的一些操作方法

  |-- report 放html测试报告的目录
    |-- xxx.html

  |-- test_case 对应xxx_page.py测试页面类的测试方法的测试类
    |-- x_test_xxx.py 继承unittest.TestCase，书写对应测试页面类的各种测试用例，失败则截图以及记录到log文件中
                      包含setUpClass/test_xxx/tearDownClass方法

  |-- run.py 运行测试用例
    |-- 加载测试用例到测试套件、运行、生成报告、发送邮件
'''
