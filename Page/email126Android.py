#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  *
from time import  sleep
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException



class Email126Page(BasePage.Page):
	"""
	android平台的网易邮箱客户端app的对象
	"""

	add_loc=(By.ID,'com.netease.mobimail:id/btn_add_account')
	email126_loc=(By.ID,'com.netease.mobimail:id/domain_126')
	username_loc=(By.ID,'com.netease.mobimail:id/editor_email')
	passwd_loc=(By.ID,'com.netease.mobimail:id/editor_password')
	loginButton_loc=(By.ID,'com.netease.mobimail:id/button_login')
	niCheng_loc=(By.NAME,'Inbox')
	me_loc=(By.ID,'com.netease.mobimail:id/tab_settings')
	setting_loc=(By.ID,'com.netease.mobimail:id/tv_mine_setting')
	emailName_loc=(By.NAME,'weiketest@126.com')
	logOut_loc=(By.NAME,'Delete Account')
	logOutOk_loc=(By.ID,'com.netease.mobimail:id/alert_dialog_btnOK')

	def clickAdd(self):
		sleep(2)
		self.find_element(*self.add_loc).click()

	def clickEmail126(self):
		sleep(2)
		self.find_element(*self.email126_loc).click()

	def userName(self,parent='login126',child='username'):
		sleep(2)
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(self.getXmlUser(parent,child))

	def password(self,parent='login126',child='passwd'):
		sleep(2)
		self.find_element(*self.passwd_loc).clear()
		self.find_element(*self.passwd_loc).send_keys(self.getXmlUser(parent,child))

	def clickLogin(self):
		sleep(2)
		self.find_element(*self.loginButton_loc).click()

	def addEmail(self):
		self.clickAdd()
		self.clickEmail126()

	def login(self):
		self.addEmail()
		self.userName()
		self.password()
		self.clickLogin()


	def getNiCheng(self):
		sleep(2)
		return self.find_element(*self.niCheng_loc).text

	def clickMe(self):
		sleep(2)
		self.find_element(*self.me_loc).click()

	def clickSetting(self):
		sleep(2)
		self.find_element(*self.setting_loc).click()

	def clickEmaiName(self):
		sleep(2)
		self.find_element(*self.emailName_loc).click()

	def clickLogOut(self):
		sleep(2)
		self.find_element(*self.logOut_loc).click()

	def clickLogOutOk(self):
		sleep(2)
		self.find_element(*self.logOutOk_loc).click()

	def clickOut(self):
		self.clickLogOut()
		self.clickLogOutOk()

	def clickQuit(self):
		self.clickMe()
		self.clickSetting()
		self.clickEmaiName()
		self.clickOut()





