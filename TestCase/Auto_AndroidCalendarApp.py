#coding:utf-8

import unittest,os,sys
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException
from appium.webdriver.common.touch_action import TouchAction
from time import  sleep
from Page import  *

class AndroidCalendar(unittest.TestCase,BasePage.Page):
	"""
	1、对Android平台的calendar进行自动化测试
	2、测试执行期间，务必启动appium的服务，android的模拟器
	3、涉及的android设备为:Google Nexus 10-5.0.0-API-21
	"""
	def setUp(self):
		self.getDesiredcaps('4.4.4','Samsung Galaxy S4','com.android.calculator2','.Calculator')

	def testAdd(self):
		'''Calendar加法运算'''
		page=CalendarAndroid.Calendar(self.driver)
		page.clickFirst()
		page.clickAdd()
		page.clickFirst()
		page.clickEq()
		text=page.getFormule()
		page.clickDigit()
		self.assertEqual(str(2),text)

	def testSub(self):
		'''Calendar减法运算'''
		page=CalendarAndroid.Calendar(self.driver)
		page.clickTwo()
		page.clickSub()
		page.clickFirst()
		page.clickEq()
		text=page.getFormule()
		page.clickDigit()
		self.assertEqual(str(1),text)

	def testMul(self):
		'''Calendar乘法运算'''
		page=CalendarAndroid.Calendar(self.driver)
		page.clickTwo()
		page.clickMul()
		page.clickFirst()
		page.clickEq()
		text=page.getFormule()
		page.clickDigit()
		self.assertEqual(str(2),text)

	def testDiv(self):
		'''Calendar除法运算'''
		page=CalendarAndroid.Calendar(self.driver)
		page.clickTwo()
		page.clickDiv()
		page.clickFirst()
		page.clickEq()
		text=page.getFormule()
		page.clickDigit()
		self.assertEqual(str(2),text)

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestSuite(unittest.makeSuite(AndroidCalendar))
	result=unittest.TextTestRunner(verbosity=2).run(suite)
	sys.exit(not result.wasSuccessful())