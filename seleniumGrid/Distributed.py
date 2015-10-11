#coding:utf-8

################################################################
#                                                              #
##################利用多线程实现分布式的自动化#######################
#                                                              #
################################################################

from selenium import  webdriver
import  time
import  threading
import  config

#启动参数(制定运行主机与浏览器)
lists={'http://127.0.0.1:7777/wd/hub':'chrome',
	   'http://127.0.0.1:6666/wd/hub':'firefox'}

#测试用例
def testBaidu(host,browser):
	print 'start:%s'%time.ctime()
	print host,browser
	driver=webdriver.Remote(
		command_executor=host,
		desired_capabilities={
			'platform':'ANY',
			'browserName':browser,
			'version':'',
			'javascriptEnable':True
		})
	driver.get('http://www.baidu.com')
	driver.maximize_window()
	driver.implicitly_wait(30)
	driver.find_element_by_id('kw').send_keys('selenium grid2')
	driver.find_element_by_id('su').click()
	time.sleep(3)
	driver.close()

threads=[]

files=range(len(config.getConfig()))

#创建线程
for host,browser in config.getConfig().items():
	t=threading.Thread(target=testBaidu,args=(host,browser))
	threads.append(t)

if __name__=='__main__':
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
	print 'end:%s'%time.ctime()

