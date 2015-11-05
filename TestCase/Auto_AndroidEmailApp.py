#coding:utf-8

import unittest,os,sys
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException
from selenium.webdriver.common.touch_actions import TouchActions
from time import  sleep
from Page import  *

class AndroidEmail(unittest.TestCase,email126Android.Email126Page):
	"""
	1、对Android平台的weibo进行自动化测试
	2、测试执行期间，务必启动appium的服务，android的模拟器
	3、涉及的android设备为:Samsung Galaxy S4-4.4.4-API-19
	"""
	def setUp(self):
		self.getAndroid('4.4.4','Samsung Galaxy S4','com.netease.mail','com.netease.mobimail.activity.StartActivity')

	def testLogin(self):
		"""
		:return:验证weibo客户端的登录
		"""
		self.login()
		text=self.getNiCheng()
		self.clickQuit()
		self.assertEqual(text,u'Inbox')

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestSuite(unittest.makeSuite(AndroidEmail))
	result=unittest.TextTestRunner(verbosity=2).run(suite)
	sys.exit(not result.wasSuccessful())