#!/usr/bin/env python
#coding:utf-8

from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import NoSuchFrameException
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.common.by import By
from selenium import  webdriver
from appium import  webdriver

class Factory:
	def createAutomation(self,page):
		if page=='web':
			return WebPage()
		elif page=='app':
			return AppPage()

class AutomationPage:
	def __str__(self):
		return 'page'

	def findElement(self,*loc):
		try:
			return self.driver.find_element(*loc)
		except(NoSuchElementException,KeyError,ValueError),e:
			print 'Error details :%s'%(e.args[0])

class WebPage(AutomationPage):
	def __str__(self):
		return 'web'

	def __init__(self,driver):
		self.driver=driver

	def goTo(self,base_url):
		self.driver.get(base_url)

	def getCurrentUrl(self):
		return self.driver.current_url

class AppPage(AutomationPage):
	def __str__(self):
		return 'app'

	def __init__(self,driver):
		self.driver=driver

	def getDesiredcaps(self,version,deviceName,package,activity):
		"""
		:param version: 设备版本
		:param deviceName: 设备名称
		:param package: apk包名称
		:param activity: apk的activity
		:return:android初始化信息
		"""
		PATH=lambda p: os.path.abspath(
			os.path.join(os.path.dirname(__file__),p)
		)
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']=version
		# desired_caps['deviceName']='Android Emulator'
		desired_caps['deviceName']=deviceName
		desired_caps['appPackage']=package
		desired_caps['appActivity']=activity
		desired_caps['waitappActivity']='android.webkit.WebView'
		desired_caps['browserName']=''
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
		self.driver.implicitly_wait(30)
