#coding:utf-8

from selenium import  webdriver
from selenium.webdriver.common.by import By
from Page import  *
from time import  sleep
from appium import  webdriver
from appium.common.exceptions import NoSuchContextException



class Calendar(BasePage.Page):
	"""
	1、对 android平台的计数器App的页面元素
	"""
	#加
	add_loc=(By.ID,'com.android.calculator2:id/plus')
	#减
	sub_loc=(By.ID,'com.android.calculator2:id/minus')
	#乘
	mul_loc=(By.ID,'com.android.calculator2:id/mul')
	#除
	div_loc=(By.ID,'com.android.calculator2:id/div')
	#==
	eq_loc=(By.ID,'com.android.calculator2:id/equal')
	#del键
	del_loc=(By.ID,'com.android.calculator2:id/del')
	#零键
	digit_loc=(By.ID,"com.android.calculator2:id/digit0")
	first_loc=(By.ID,"com.android.calculator2:id/digit1")
	two_loc=(By.ID,"com.android.calculator2:id/digit2")
	nine_loc=(By.ID,'com.android.calculator2:id/digit9')
	formila_loc=(By.CLASS_NAME,'android.widget.EditText')

	def clickAdd(self):
		sleep(2)
		self.find_element(*self.add_loc).click()

	def clickSub(self):
		sleep(2)
		self.find_element(*self.sub_loc).click()

	def clickMul(self):
		sleep(2)
		self.find_element(*self.mul_loc).click()

	def clickDiv(self):
		sleep(2)
		self.find_element(*self.div_loc).click()

	def clickEq(self):
		sleep(2)
		self.find_element(*self.eq_loc).click()

	def clickDel(self):
		sleep(2)
		self.find_element(*self.del_loc).click()

	def clickDigit(self):
		sleep(2)
		self.find_element(*self.digit_loc).click()

	def clickFirst(self):
		sleep(2)
		self.find_element(*self.first_loc).click()

	def clickTwo(self):
		sleep(2)
		self.find_element(*self.two_loc).click()

	def clickNine(self):
		sleep(2)
		self.find_element(*self.nine_loc).click()

	def getFormule(self):
		sleep(2)
		return self.find_element(*self.formila_loc).text

