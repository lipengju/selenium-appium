#coding:utf-8

from selenium import  webdriver
from time import  sleep
import  unittest,csv,sys,os,threading,xlrd
from Page import  *
from ddt import  ddt,data,unpack
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

@ddt
class baiduTest(unittest.TestCase,BasePage.Page):
	def setUp(self,value='baiduUrl'):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get(self.getXmlData(value))

	@data((u'admin',u'请您填写密码'),('@$@#%',u'请您填写密码'),('a',u'请您填写密码'))
	@unpack
	def testData1(self,actualValue,expectedValue):
		'''百度登录来演示ddt模块使用'''
		baidu=baiduPage.baiduLogin(self.driver)
		baidu.clickLogin()
		baidu.inputUserName(actualValue)
		baidu.clickLoginButton()
		errorText=baidu.getError()
		self.assertEqual(errorText,expectedValue)

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(baiduTest)
	unittest.TextTestRunner(verbosity=2).run(suite)


