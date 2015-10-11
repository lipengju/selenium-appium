#coding:utf-8

#已新浪邮箱登录为案例

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  *
import  time

class singLogin(BasePage.Page):


	username_loc=(By.ID,'freename')
	passwd_loc=(By.ID,'freepassword')
	cancelAuto_loc=(By.ID,'store1')
	login_loc=(By.CLASS_NAME,'loginBtn')
	niCheng_loc=(By.XPATH,".//*[@id='user_id']/em[2]")
	exit_loc=(By.XPATH,".//*[@id='warpMain']/div[4]/div[1]/div[3]/div[3]/span/a")


	rsmsName_loc=(By.NAME,'login_id')
	rsmsPasswd_loc=(By.NAME,'password')
	rsmsLogin_loc=(By.CLASS_NAME,'button')
	rsmsNiCheng_loc=(By.CSS_SELECTOR,".loginName")


	def inputUsername(self,value):
		self.find_element(*self.username_loc).send_keys(value)
		time.sleep(1)

	def inputPasswd(self,value):
		self.find_element(*self.passwd_loc).send_keys(value)
		time.sleep(1)

	def clickStore(self):
		self.find_element(*self.cancelAuto_loc).click()


	def clickLogin(self):
		self.find_element(*self.login_loc).click()

	def loginSina(self,parent='loginSina',child1='username',child2='passwd'):
		self.inputUsername(self.getXmlUser(parent,child1))
		self.inputPasswd(self.getXmlUser(parent,child2))
		self.clickStore()
		self.clickLogin()

	def getNiCheng(self):
		return self.find_element(*self.niCheng_loc).text

	def clickExit(self):
		self.find_element(*self.exit_loc).click()
		time.sleep(3)


	def rsmsName(self,value):
		self.find_element(*self.rsmsName_loc).send_keys(value)
		time.sleep(1)


	def rsmsPasswd(self,value):
		self.find_element(*self.rsmsPasswd_loc).send_keys(value)
		time.sleep(1)


	def clickRsms(self):
		self.find_element(*self.rsmsLogin_loc).click()

	def getRsmsNiCheng(self):
		time.sleep(2)
		return self.find_element(*self.rsmsNiCheng_loc).text