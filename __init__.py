"""
__author__ = 'LZL'
__mtime__ = '2018/7/16'
Config配置文件目录
	config.ini 配置文件
	globalconfig.py 获得日志路径、测试用例路径、测试报告路径、测试数据路径
	__init__.py


Data测试数据
	TestData.xlsx 测试数据

Log日志
	Log.py 日志类。设置日志类，其他模块或文件需要日志类时调用该文件

Public公共文件库
	common 封装的公共方法，操作excel
		Commonconfig.py 公共的参数配置，调试过程中的测试数据等
		DoExcel.py 操作excel（数据驱动）
		Send_email.py 发送邮件（附件）
		ReadConfigini.py 读取ini格式的配置文件
		TestCaseinfo.py 测试用例信息（常量类）
		Report.py 测试报告的类
	Pages 使用po模式设计的测试页面
		BasePage.py：基类，对一些测试页面公共方法、属性的封装及webdriver一些方法的二次封装
		xxx.py：各个独立UI页面的方法

Report测试报告
	Log日志目录
		xxxxx.log 日志文件
	TestReport测试报告目录
		xxxx.html 测试报告

TestCase测试用例
	Tc_xxx.py 各个测试用例

Run.py 控制测试用例的运行
"""