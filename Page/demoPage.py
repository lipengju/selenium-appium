#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  dashPage
import  time

class demoWebPage(dashPage.WebPage):
	username_loc=(By.ID,'l-1')
	password_loc=(By.ID,'l-2')
	loginButton_loc=(By.ID,'l-4')

	def inputUserName(self,username):
		self.findElement(*self.username_loc).send_keys(username)
		time.sleep(2)

	def inputPasswd(self,password):
		self.findElement(*self.password_loc).send_keys(password)
		time.sleep(2)

	def clickLogin(self):
		self.findElement(*self.loginButton_loc).click()
		time.sleep(2)

	def login(self,username='admin',password='admin'):
		self.goTo('http://my.weke.com/login.html')
		self.inputUserName(username)
		self.inputPasswd(password)
		self.clickLogin()
