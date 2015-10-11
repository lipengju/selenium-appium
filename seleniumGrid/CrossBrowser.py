#coding:utf-8

################################################################
#                                                              #
#####################实现多浏览器多平台的测试#######################
#                                                              #
################################################################


import  time
from selenium import  webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  config
import  threading

#通过host,browser来参数化脚本
for host,browser in config.getconfig().items():
	print host
	print browser
	driver=webdriver.Remote(
		command_executor=host,
		desired_capabilities={
			'platform':'ANY',
			'browserName':browser,
			'version':'',
			'javascriptEnabled':True
		}
	)
	driver.get('http://www.baidu.com')
	driver.maximize_window()
	driver.implicitly_wait(30)
	driver.find_element_by_id('kw').send_keys('selenium grid2')
	time.sleep(3)
	driver.close()




