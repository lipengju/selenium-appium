#coding:utf-8

#百度首页测试案例

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  *
from time import  sleep

class baiduLogin(BasePage.Page):

	so_loc=(By.ID,'kw')
	login_loc=(By.LINK_TEXT,u'登录')
	loginUser_loc=(By.ID,'TANGRAM__PSP_8__userName')
	userError_loc=(By.XPATH,".//*[@id='TANGRAM__PSP_8__error']")
	loginPasswd_loc=(By.ID,'TANGRAM__PSP_8__password')
	loginButton_loc=(By.ID,'TANGRAM__PSP_8__submit')

	def inputSo(self,value):
		self.find_element(*self.so_loc).send_keys(value)
		sleep(1)

	def clickLogin(self):
		sleep(2)
		self.find_element(*self.login_loc).click()
		sleep(3)

	def inputUserName(self,username):
		sleep(2)
		self.find_element(*self.loginUser_loc).clear()
		self.find_element(*self.loginUser_loc).send_keys(username)

	def inputPasswd(self,passwd):
		sleep(2)
		self.find_element(*self.loginPasswd_loc).clear()
		self.find_element(*self.loginPasswd_loc).send_keys(passwd)

	def clickLoginButton(self):
		sleep(1)
		self.find_element(*self.loginButton_loc).click()

	def getError(self):
		sleep(2)
		return self.find_element(*self.userError_loc).text