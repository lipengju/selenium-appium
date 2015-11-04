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
