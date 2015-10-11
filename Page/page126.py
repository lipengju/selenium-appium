#coding:utf-8
#/usr/bin/python

####################################################################
#                                                                  #
######################126邮箱页面对象################################
#                                                                  #
####################################################################

from Page import  *
from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import  sleep,ctime


class email126(BasePage.Page):

	username_loc=(By.ID,'idInput')
	passwd_loc=(By.ID,'pwdInput')
	login_loc=(By.ID,'loginBtn')
	niCheng_loc=(By.XPATH,".//*[@id='spnUid']")
	exit_loc=(By.XPATH,".//*[@id='_mail_component_33_33']/a")

	def inputUsername(self,value):
		self.find_element(*self.username_loc).send_keys(value)
		sleep(2)

	def inputPasswd(self,value):
		self.find_element(*self.passwd_loc).send_keys(value)
		sleep(2)

	def clickLogin(self):
		self.find_element(*self.login_loc).click()
		sleep(2)

	def getCheng(self):
		sleep(3)
		return self.find_element(*self.niCheng_loc).text


	def clickExit(self):
		self.find_element(*self.exit_loc).click()
		sleep(2)

	def login(self,parent='login126',child1='username',child2='passwd'):
		self.inputUsername(self.getXmlUser(parent,child1))
		self.inputPasswd(self.getXmlUser(parent,child2))
		self.clickLogin()






