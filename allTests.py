#!-*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import unittest
import HTMLTestRunner
import time
import  os
from  email.mime.text import MIMEText
from email.mime.multipart import  MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import  Header
from email.utils import  parseaddr,formataddr
import smtplib


#发送邮件
def sentMail(newFile,from_addr='SINA email account',passwd='SINA email account password',smtp_server='smtp.sina.com',to_addr='QQ mailbox'):
    #邮件正文
    f=open(newFile,'rb')
    mailContent=f.read()
    f.close()
    msg=MIMEText(mailContent,_subtype='html',_charset='utf-8')
    msg['From']=from_addr
    msg['To']=to_addr
    msg['Subject']=u'Automation Test Report'

    #定义发送时间
    msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %z')
    server=smtplib.SMTP(smtp_server,25)
    # server.set_debuglevel(1)
    server.login(from_addr,passwd)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
    print u'Mail sent successfully'

#找到最新的测试报告
def sendReport():
    result_dir='D:/git/PyCharm/SeleniumHq/Test-report'
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    print u'最新测试报告:',lists[-1]

    #找到最新的文件
    newFile=os.path.join(result_dir,lists[-1])
    print newFile
    #调用发邮件模块
    sentMail(newFile)



listTestCase='D:\\git\\PyCharm\\SeleniumHq\\TestCase'

def createSuite():
	testunit=unittest.TestSuite()

	#测试加载器
	discoverage=unittest.defaultTestLoader.discover(
		listTestCase,
		pattern='Auto_*.py',
		top_level_dir=None
	)

	#添加测试模块
	for testSuite in discoverage:
		for testCase in testSuite:
			testunit.addTests(testCase)
			print testunit
	return testunit

allTestNames=createSuite()
#获取当前时间
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

#自动化测试报告
filename='Test-report/'+now+'Report.html'
fp=file(filename,'wb')
runner=HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title=u'SELENIUM WEBDRIVER AUTOMATION WEB TEST REPORT',
	description=u'AUTOMATION WEB TEST REPORT'
)

runner.run(allTestNames)
fp.close()
sendReport()
sys.exit()

#控制脚本执行的时间,注意：设置的时间必须大于当前的时间
# k=1
# while k<2:
# 	timeing=time.strftime('%H_%M',time.localtime())
# 	if timeing=='12_50':
# 		print u'Start test execution scripts'
# 		runner.run(allTestNames)
# 		print u'Test scripts finish to exit'
# 		break
# 	else:
# 		time.sleep(5)
# 		print timeing
# fp.close()
# sendReport()




