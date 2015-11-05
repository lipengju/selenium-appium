#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  dashPage
from appium import  webdriver
import  time

class demoAndroidPage(dashPage.AppPage):
	login_loc=(By.ID,'com.sina.weibo:id/titleSave')
	userName_loc=(By.ID,'com.sina.weibo:id/etLoginUsername')
	password_loc=(By.ID,'com.sina.weibo:id/etPwd')
	loginButton_loc=(By.ID,'com.sina.weibo:id/bnLogin')

	def clickLogin(self):
		self.findElement(*self.login_loc).click()
		time.sleep(2)

	def inputUserName(self,username):
		self.findElement(*self.userName_loc).send_keys(username)
		time.sleep(2)

	def inputPasswd(self,password):
		self.findElement(*self.password_loc).send_keys(password)
		time.sleep(2)

	def clickLoginButton(self):
		self.findElement(*self.loginButton_loc).click()
		time.sleep(2)

	def login(self,username='admin',password='admin'):
		self.clickLogin()
		self.inputUserName(username)
		self.inputPasswd(password)
		self.clickLoginButton()
