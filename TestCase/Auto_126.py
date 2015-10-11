#coding:utf-8
#/usr/bin/python


from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from time import  sleep,time,ctime
import  unittest
from Page import  *
import  threading
import  logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True


class Page126(unittest.TestCase,BasePage.Page):
	def setUp(self,value='url126'):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get(self.getXmlData(value))

	def testLogin(self,value='niCheng'):
		'''126邮箱登录验证'''
		page=page126.email126(self.driver)
		page.login()
		text=page.getCheng()
		page.clickExit()
		self.assertEqual(text,self.getXmlData(value))

	def testTitle(self,value='title126',value2='browserFirefox'):
		'''126邮箱title验证'''
		self.assertEqual(self.driver.title,self.getXmlData(value))

	def tearDown(self):
		self.driver.close()
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(Page126)
	unittest.TextTestRunner(verbosity=2).run(suite)


