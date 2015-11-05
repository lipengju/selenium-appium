#coding:utf-8

import unittest,os,sys
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException
from selenium.webdriver.common.touch_actions import TouchActions
from time import  sleep
from Page import  dashPage,demoAppPage

class AndroidSina(unittest.TestCase,demoAppPage.demoAndroidPage,dashPage.AppPage):
	def setUp(self):
		self.getDesiredcaps('4.4.4','Samsung Galaxy S4','com.sina.weibo','com.sina.weibo.MainTabActivity')

	def testLogin(self):
		self.login()

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestSuite(unittest.makeSuite(AndroidSina))
	result=unittest.TextTestRunner(verbosity=2).run(suite)
	sys.exit(not result.wasSuccessful())