#coding:utf-8

from selenium import  webdriver
from selenium.common.exceptions import *
from time import  sleep,time,ctime
import  unittest
from Page import  dashPage,demoPage
import  time
import  logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True

class singPage(unittest.TestCase):
	def setUp(self):
		self.driver=webdriver.Firefox()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)

	def testTitle(self):
		page=demoPage.demoWebPage(self.driver)
		page.login()

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	unittest.main(verbosity=2)
