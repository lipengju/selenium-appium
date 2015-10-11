#coding:utf-8

import unittest,os,sys
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException
from selenium.webdriver.common.touch_actions import TouchActions
from time import  sleep
from Page import  *

class AndroidWeiBo(unittest.TestCase,weiboAndroid.WeiBoPage):
	"""
	1、对Android平台的weibo进行自动化测试
	2、测试执行期间，务必启动appium的服务，android的模拟器
	3、涉及的android设备为:Samsung Galaxy S4-4.4.4-API-19
	"""
	def setUp(self):
		self.getDesiredcaps('4.4.4','Samsung Galaxy S4','com.sina.weibo','com.sina.weibo.MainTabActivity')

	def testLogin(self):
		"""
		:return:验证weibo客户端的登录
		"""
		self.loginWeiBo()
		text=self.getNiCheng()
		self.exitWeiBo()
		self.assertEqual(text,u'和而不统')

	def testMe(self):
		"""
		:return:验证点击Me后，跳转的页面
		"""
		self.loginWeiBo()
		self.clickMe()
		text=self.getMe()
		self.clickSetting()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'Me')


	def testSetting(self):
		"""
		:return:验证点击setting后，跳转的页面
		"""
		self.loginWeiBo()
		self.clickMe()
		self.clickSetting()
		text=self.getSetting()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'Settings')


	def testVersion(self):
		"""
		:return:验证about weibo
		"""
		self.loginWeiBo()
		self.clickMe()
		self.clickSetting()
		self.clickVersion()
		text=self.getVersion()
		self.clickBack()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'Weibo Service Agreement')


	def testFollow(self):
		"""
		:return:点击weobo的Follow
		"""
		self.loginWeiBo()
		self.clickMe()
		text=self.getFollow()
		self.clickSetting()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'')


	def testFollower(self):
		"""
		:return:点击weobo的Follower
		"""
		self.loginWeiBo()
		self.clickMe()
		text=self.getFollower()
		self.clickSetting()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'')


	def testAbout(self):
		"""
		:return:点击weobo的About
		"""
		self.loginWeiBo()
		self.clickMe()
		text=self.getAbout()
		self.clickSetting()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'About:君子和而不同！乐观，积极的心态来迎接每天的新生活。')


	def testCatch(self):
		"""
		:return:点击weobo的catch处理
		"""
		self.loginWeiBo()
		self.clickMe()
		self.clickSetting()
		self.clickClearCatch()
		text=self.getCatchSize()
		self.clickAccount()
		self.clickLogOut()
		self.assertEqual(text,u'0.0MB')

	def testExit(self):
		"""
		:return:验证weibo客户端的退出
		"""
		self.loginWeiBo()
		self.exitWeiBo()

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestSuite(unittest.makeSuite(AndroidWeiBo))
	result=unittest.TextTestRunner(verbosity=2).run(suite)
	sys.exit(not result.wasSuccessful())