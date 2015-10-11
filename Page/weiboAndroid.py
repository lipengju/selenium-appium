#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  *
from time import  sleep
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException



class WeiBoPage(BasePage.Page):
	"""
	android平台的微博客户端app的对象
	"""

	login_loc=(By.ID,'com.sina.weibo:id/titleSave')
	username_loc=(By.ID,'com.sina.weibo:id/etLoginUsername')
	password_loc=(By.ID,'com.sina.weibo:id/etPwd')
	loginButton_loc=(By.ID,'com.sina.weibo:id/bnLogin')
	inwei_loc=(By.ID,'com.sina.weibo:id/iv_navigater_clickable')
	niCheng_loc=(By.ID,u'com.sina.weibo:id/tvNick')
	me_loc=(By.XPATH,"//android.view.View[4]")
	follow_loc=(By.ID,'com.sina.weibo:id/cabFollow')
	follower_loc=(By.ID,'com.sina.weibo:id/cabFan')
	about_loc=(By.ID,'com.sina.weibo:id/tvVerifyInfo')
	meText_loc=(By.ID,'com.sina.weibo:id/titleText')
	setting_loc=(By.ID,'com.sina.weibo:id/titleSave')
	catch_loc=(By.ID,'com.sina.weibo:id/cleanCacheContent')
	catchSize_loc=(By.ID,'com.sina.weibo:id/cleanCacheSize')
	settingText_loc=(By.ID,'com.sina.weibo:id/titleText')
	version_loc=(By.ID,'com.sina.weibo:id/moreAboutContent')
	versionText_loc=(By.ID,'com.sina.weibo:id/service')
	back_loc=(By.ID,'com.sina.weibo:id/titleBack')
	account_loc=(By.ID,'com.sina.weibo:id/accountLayout')
	logOut_loc=(By.ID,'com.sina.weibo:id/exitAccountContent')
	logOutOk_loc=(By.NAME,"OK")
	logOutCancel_loc=(By.NAME,'Cancel')



	def clickLogin(self):
		sleep(2)
		self.find_element(*self.login_loc).click()

	def inputUserName(self,login='loginSina',username='username'):
		sleep(2)
		self.find_element(*self.username_loc).clear()
		self.find_element(*self.username_loc).send_keys(self.getXmlUser(login,username))

	def inputPasswd(self,login='loginSina',password='passwd'):
		sleep(2)
		self.find_element(*self.password_loc).clear()
		self.find_element(*self.password_loc).send_keys(self.getXmlUser(login,password))

	def clickLoginButton(self):
		sleep(2)
		self.find_element(*self.loginButton_loc).click()

	def clickInWei(self):
		sleep(2)
		self.find_element(*self.inwei_loc).click()

	def getNiCheng(self):
		sleep(3)
		return self.find_element(*self.niCheng_loc).text

	def loginWeiBo(self):
		self.clickLogin()
		self.inputUserName()
		self.inputPasswd()
		self.clickLoginButton()
		sleep(3)

	def clickMe(self):
		sleep(2)
		self.find_element(*self.me_loc).click()

	def getMe(self):
		sleep(2)
		return self.find_element(*self.meText_loc).text

	def getFollow(self):
		sleep(2)
		return self.find_element(*self.follow_loc).text

	def getFollower(self):
		sleep(2)
		return self.find_element(*self.follower_loc).text

	def getAbout(self):
		sleep(2)
		return self.find_element(*self.about_loc).text

	def clickSetting(self):
		sleep(2)
		self.find_element(*self.setting_loc).click()

	def clickAccount(self):
		sleep(2)
		self.find_element(*self.account_loc).click()

	def clickClearCatch(self):
		sleep(2)
		self.find_element(*self.catch_loc).click()
		self.clickLogOutOk()

	def getCatchSize(self):
		sleep(2)
		return self.find_element(*self.catchSize_loc).text
	def getSetting(self):
		sleep(2)
		return self.find_element(*self.settingText_loc).text

	def clickVersion(self):
		sleep(2)
		self.find_element(*self.version_loc).click()

	def getVersion(self):
		sleep(2)
		return self.find_element(*self.versionText_loc).text

	def clickBack(self):
		sleep(2)
		self.find_element(*self.back_loc).click()

	def clickLogOut(self):
		sleep(2)
		self.find_element(*self.logOut_loc).click()
		self.clickLogOutOk()

	def clickLogOutOk(self):
		sleep(2)
		self.find_element(*self.logOutOk_loc).click()

	def clickLogOutCancel(self):
		sleep(2)
		self.find_element(*self.logOutCancel_loc).click()


	def exitWeiBo(self):
		self.clickMe()
		self.clickSetting()
		self.clickAccount()
		self.clickLogOut()
		sleep(2)

