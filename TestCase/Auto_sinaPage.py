#coding:utf-8

from selenium import  webdriver
from selenium.common.exceptions import *
from time import  sleep,time,ctime
import  unittest
from Page import  *
import  time
import  logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

class singPage(unittest.TestCase,BasePage.Page):
	def setUp(self,value='urlSina'):
		self.driver=self.browser('firefox')
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get(self.getXmlData(value))

	def testLogin(self,value='ChengSina'):
		'''新浪邮箱登录测试'''
		page=sinaPage.singLogin(self.driver)
		page.loginSina()
		text=page.getNiCheng()
		page.clickExit()
		self.assertEqual(text,self.getXmlData(value))

	def testTitle(self,value='sinaTitle'):
		'''新浪邮箱title验证'''
		self.assertEqual(self.driver.title,self.getXmlData(value))


	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(singPage)
	unittest.TextTestRunner(verbosity=2).run(suite)
