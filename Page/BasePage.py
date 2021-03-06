#coding:utf-8
#!/usr/bin/python

from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import NoSuchFrameException
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.common.by import By
from selenium import  webdriver
from appium import  webdriver
import  xml.dom.minidom,os,glob
import  csv,xlrd,threading,os,sys
import  urllib,urlparse,HTMLParser ,sgmllib
from time import  sleep

class Page(object):
	kb_url='http://www.baidu.com'
	def __init__(self,selenium_driver,base_url=kb_url,parent=None):
		"""
		对object page的Page类进行实例化
		:param selenium_driver:webdriver
		:param base_url:测试的url
		:param parent:
		:return:
		"""
		self.base_url=base_url
		self.driver=selenium_driver
		self.timeout=30
		self.parent=parent
		self.tabs={}

	def _open(self,url):
		url=self.base_url+url
		self.driver.get(url)

	def find_element(self,*loc):
		try:
			return  self.driver.find_element(*loc)
		except (NoSuchElementException,KeyError,ValueError,Exception),e:
			print 'Error details:%s'%(e.args[0])


	def open(self):
		self._open(self.url)

	def on_page(self):
		return self.driver.current_url==(self.base_url+self.url)

	#文件目录
	def data_dirs(self):
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		TEMPLATE_DIRS = (
		os.path.join(BASE_DIR,  'Data-driven'),
		)
		d='/'.join(TEMPLATE_DIRS)
		return d

	def getCurrentUrl(self):
		return self.driver.current_url

	def scriptKJs(self,src):
		"""
		执行js的代码
		:param src: js的代码
		:return:
		"""
		return self.driver.execute_script(src)

	def getXmlData(self,value):
		"""
		使用dom获取xml节点的数据
		:param value:
		:return:
		"""
		dom=xml.dom.minidom.parse(self.data_dirs()+"\\systemXml.xml")
		db=dom.documentElement
		name=db.getElementsByTagName(value)
		nameValue=name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent,child):
		"""
		获取xml中的子节点的数据
		:param parent:父节点
		:param child:子节点
		:return:
		"""
		dom=xml.dom.minidom.parse(self.data_dirs()+"\\systemXml.xml")
		db=dom.documentElement
		itemlist=db.getElementsByTagName(parent)
		item=itemlist[0]
		return item.getAttribute(child)


	def browser(self,Browser):
		"""
		:param Browser: browser name
		:return:浏览器多平台的处理
		"""
		driver=webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
								desired_capabilities={'platform':'ANY',
													  'browserName':Browser,
													  'version':'',
													  'javascriptEnabled':True,
													  })
		return driver


	def getCsvData(self,value1,value2):
		"""
		:param file_name: csv文件的路劲
		:return:csv文件中每列的数据
		"""
		rows=[]
		with open(self.data_dirs()+"\\testData.csv",'rb') as csvfile:
			db=csv.reader(csvfile,delimiter=',',quotechar='|')
			next(db,None)
			for row in db:
				rows.append(row)
			return rows[value1][value2]

	def getCsvDdt(self):
		"""
		:param file_name: csv文件de路劲
		:return:返回csv文件的数据,结合ddt模块
		"""
		rows=[]
		with open(self.data_dirs()+"\\testData.cs",'rb')  as f:
			readers=csv.reader(f,delimiter=',',quotechar='|')
			next(readers,None)
			for row in readers:
				rows.append(row)
			return rows


	def getExcelData(self):
		"""
		:return:返回excel文件中数据，结合ddt模块
		"""
		rows=[]
		book=xlrd.open_workbook(self.data_dirs()+"\\testData.xls")
		sheet=book.sheet_by_index(0)
		for row in range(1,sheet.nrows):
			rows.append(list(sheet.row_values(row,0,sheet.ncols)))
		return rows


	def getExcelDdt(self,rowValue,colValue):
		"""
		:param file_name: excel文件的路劲
		:return:返回excel每列的数据
		"""
		book=xlrd.open_workbook(self.data_dirs()+"\\testData.xlsx")
		sheet=book.sheet_by_index(0)
		return sheet.row_values(rowValue,colValue)


	def getAndroid(self,version,deviceName,package,activity):
		"""
		:param version: 设备版本
		:param deviceName: 设备名称
		:param package: apk包名称
		:param activity: apk的activity
		:return:android初始化信息
		"""
		PATH=lambda p: os.path.abspath(
			os.path.join(os.path.dirname(__file__),p)
		)
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']=version
		# desired_caps['deviceName']='Android Emulator'
		desired_caps['deviceName']=deviceName
		desired_caps['appPackage']=package
		desired_caps['appActivity']=activity
		desired_caps['waitappActivity']='android.webkit.WebView'
		desired_caps['browserName']=''
		self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
		self.driver.implicitly_wait(30)

	def getServerAndroid(self,version,deviceName,package,activity):
		"""
		:param version: 设备版本
		:param deviceName: 设备名称
		:param package: apk的package
		:param activity: apk的activity
		:return:多平台执行(需要selenium-server)
		"""
		PATH=lambda p: os.path.abspath(
			os.path.join(os.path.dirname(__file__),p)
		)
		self.driver=None
		capabilities={
			'platformName':'Android',
			'platformVersion':version,
			'deviceName':deviceName,
			'appPackage':package,
			'appActivity':activity,
			'unicodeKeyboard':True,
			'resetKeyboard':True}
		self.driver=webdriver.Remote('http://127.0.0.1/wd/hub',capabilities)
		self.driver.implicitly_wait(30)

	def urlcheck(self,value='baiduUrl'):
		"""
		对html的解析，验证url的地址是否合法
		:param value:
		:return:
		"""
		check_urls=['index','test','help','news','faq','download']
		for url in check_urls:
			new_url=urlparse.urljoin(self.getXmlData(value),url)
			fp=urllib.urlopen(new_url)
			data=fp.read()
			fp.close()

			per=checkHtml()
			#获取解析的数据
			per.feed(data)
			per.close()

			#判断url
			if per.available:
				print new_url,'===>Ok'
			else:
				print new_url,'===>Not Found'


	def urlLink(self,value='baiduUrl'):
		f=urllib.urlopen(self.getXmlData(value))
		data=f.read()
		f.close()

		ld=LinkCheck()
		ld.feed(data)

		for i ,link in  enumerate(ld.links):
			print i,'====>',link

class checkHtml(HTMLParser.HTMLParser):
	available=True
	def handle_data(self, data):
		if '404 Not Found' in data or 'Error 404' in data:
			self.available=False
		else:
			pass

class LinkCheck(sgmllib.SGMLParser):
	def __init__(self):
		sgmllib.SGMLParser.__init__(self)
		self.links=[]

	#处理a标签
	def start_a(self,attributes):
		for link in attributes:
			tag,attr=link[:2]
			if tag=='href':
				self.links.append(attr)









