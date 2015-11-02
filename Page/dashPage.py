#!/usr/bin/env python
#coding:utf-8

class Factory:
	def createAutomation(self,page):
		if page=='web':
			return WebPage()
		elif page=='app':
			return AppPage()

class AutomationPage:
	def __str__(self):
		return 'page'

class WebPage(AutomationPage):
	def __str__(self):
		return 'web'

	def share(self):
		print u'我是全部可以调用的,'

	def getWeb(self):
		print u'web自动化测试'

class AppPage(AutomationPage):
	def __str__(self):
		return 'app'

	def getApp(self):
		print u'移动平台自动化测试'

if __name__=='__main__':
	factory=Factory()
	web=factory.createAutomation('web')
	web.getWeb()
	web.share()