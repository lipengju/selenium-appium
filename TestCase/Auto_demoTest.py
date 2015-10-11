#coding:utf-8

from selenium import  webdriver
from time import  sleep,time,ctime
import  unittest
from Page import  *
import  threading
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
DesiredCapabilities.INTERNETEXPLORER['ignoreProtectedModeSettings'] = True


class DemoPage(unittest.TestCase,BasePage.Page):
	def setUp(self,value='baiduUrl'):
		self.driver=webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get(self.getXmlData(value))

	def testTitle(self,value='testData'):
		'''百度title验证'''
		self.assertTrue(self.driver.title  in  self.getXmlData(value) )

	def testUrl(self,value='baiduUrl'):
		'''百度url验证'''
		self.assertEqual(self.driver.current_url,self.getXmlData(value))
		self.urlcheck()
		self.urlLink()

	def testCSV(self):
		page=baiduPage.baiduLogin(self.driver)
		page.inputSo(self.getCsvData(1,0))

	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	suite=unittest.TestLoader().loadTestsFromTestCase(DemoPage)
	unittest.TextTestRunner(verbosity=2).run(suite)


