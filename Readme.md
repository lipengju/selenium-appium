测试框架的职责：
1、定义统一的方式来编写和组织测试用例
2、集成不同的测试驱动技术
3、控制测试用例的执行过程
4、生成测试报告和测试日志


代码覆盖率的统计结果如下：

coverage run allTests.py
coverage report
coverage html -d covhtml
coverage combine


Page Objects如下：
Within your web app's UI there are areas that your tests interact with. A Page Object simply models these as objects within
the test code. This reduces the amount of duplicated code and means that if the UI changes, the fix need only be applied in
one place.
ZH:
在您的 web 应用程序的用户界面内有您的测试与交互的领域。Page 对象只是模型这些作为测试代码中的对象。这减少了重复代码，意味着，如果用户界面发生改变，
需要只在一个地方应用修补程序。

Implementation Notes(实现说明):
PageObjects can be thought of as facing in two directions simultaneously. Facing towards the developer of a test, they represent
the services offered by a particular page. Facing away from the developer, they should be the only thing that has a deep knowledge
of the structure of the HTML of a page (or part of a page) It's simplest to think of the methods on a Page Object as offering
the "services" that a page offers rather than exposing the details and mechanics of the page. As an example, think of the inbox
of any web-based email system. Amongst the services that it offers are typically the ability to compose a new email, to choose
to read a single email, and to list the subject lines of the emails in the inbox. How these are implemented shouldn't matter to
the test.
Because we're encouraging the developer of a test to try and think about the services that they're interacting with rather than
the implementation, PageObjects should seldom expose the underlying WebDriver instance. To facilitate this, methods on the
PageObject should return other PageObjects. This means that we can effectively model the user's journey through our application.
It also means that should the way that pages relate to one another change (like when the login page asks the user to change their
password the first time they log into a service, when it previously didn't do that) simply changing the appropriate method's
signature will cause the tests to fail to compile. Put another way, we can tell which tests would fail without needing to run
them when we change the relationship between pages and reflect this in the PageObjects.
ZH:
PageObjects 可以看作是同时面对两个方向。面向开发人员的测试，他们代表某一网页所提供的服务。面对对开发人员，他们应该是唯一具有深的知识结构的 HTML 页面
(或网页的部分) 的最简单想网页的页面对象上作为提供"服务"，方法是提供，而不是暴露的详细信息和页面的力学。作为一个例子，认为任何基于 web 的电子邮件系统的
收件箱中。它提供的服务之间通常是撰写新邮件，选择阅读一封电子邮件，并列出在收件箱中邮件的主题行的能力。这些如何实现对测试的问题。
因为我们鼓励开发人员测试的尝试，并认为有关的服务，而不执行它们相互作用，PageObjects 应该很少公开基础 WebDriver 实例。为此，PageObject 方法应返回其
他 PageObjects。这意味着，我们可以有效的模拟用户的旅程通过我们的应用程序。这也意味着，页面涉及到另一个变动 (比如登录页要求用户更改他们的密码第一次当他
们登录到服务，当它以前没有做到) 简单的方式应该改变相应的方法的签名会导致编译失败的测试。把另一种方式，我们可以告诉哪些测试会失败而无需运行它们，当我们改
变页面之间的关系，反映出这一点的 PageObjects。


selenium grid2实现方式总结如下：
  1、多浏览器的实现方式：
      a、启动selenium-server-standalone-2.45.0.jar
      b、java -jar selenium-server-standalone-2.45.0.jar
      c、执行文件TestCase/seleniumGrid文件，可以实现多浏览器的执行

  2、多节点执行用例:
      a、启动一个hub和node(节点)
      b、启动hub的命令为：java -jar  selenium-server-standalone-2.45.0.jar  -role hub
      c、启动节点:java -jar selenium-server-standalone-2.45.0.jar -role node  -port 6666
      d、java -jar selenium-server-standalone-2.45.0.jar -role node  -port 7777
      e、具体见配置文件seleniumGrid/config.py
      f、实现代码具体见se_server.py
      g、在启动的终端启动需要满足如下的条件：
          a)、本地hub主机与远程node主机之间互相ping通
          b)、远程主机必须安装脚本的运行环境(python,selenium,浏览器以及浏览器驱动)
          c)、远程主机必须安装java环境
          d)、远程主机必须安装selenium server且启动
          e)、操作步骤汇总如下：
              a))、启动主机hub:java -jar  selenium-server-standalone-2.45.0.jar -role hub
              b))、远程启动主机:java -jar selenium-server-standalone-2.45.0.jar  -role node -port 6666
              c))、远程启动主机:java -jar selenium-server-standalone-2.45.0.jar  -role node -port 7777

  3、分布式并行运行脚本:


Appium定位元素汇总如下：
id                 -->resource-id      --->driver.find_element_by_id('id')
name               -->text             --->driver.find_element_by_name('name')
className          -->class            --->driver.find_element_by_class_name('class')
AccessibilityId    -->content-desc     --->driver.find_element_by_accessibility_id('content-desc')
cssSelector
xpath
AndroidUIAutomator -->driver.find_element_by_android_uiautomator("newUiSelector().resourceId('id')") or driver.find_element_by_android_uiautomator("UiSelector().description('content-desc')")



webView的处理方式见如下(重点是定位)：
1、先获取所有窗口的句柄，并把所有的窗口句柄输出
2、打开web view
3、进入操作里面的元素，见如下的java代码：

		//输出web view 
		java.util.Set<String> contexts=driver.getContextHandles();
		for(String context:contexts)
		{
			System.out.println(context);
		}
		
		Thread.sleep(3000);
		
		//打开web view
		driver.context("NATIVE_APP");
		driver.context("WEBVIEW_com.example.hybridtestapp");
		
		//进入web view后，我们依据名称来找到输入框，我们依据名称查找元素
		WebElement fristName=driver.findElement(By.name("fname"));
		fristName.clear();
		fristName.sendKeys("test");
		
		driver.findElement(By.id("register")).click();

#-------------------------------------------------#
#        TouchAction-->long_press                 #
#-------------------------------------------------#
appium-long press(长按):
长按是一个移动的手势，得使用TouchAction类的长按示例。导入的包为；
from appium.webdriver.common.touch_action import TouchAction

实例代码见如下的测试脚本：
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,unittest,sys,os


desired_caps={}
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['platformVersion']='4.4.4'
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='com.android.dialer'
desired_caps['appActivity']='com.android.dialer.DialtactsActivity'
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

#拨号键盘来演示long_press的使用
driver.find_element_by_accessibility_id('dial pad').click()
time.sleep(3)

#拨号键盘长按0，会变为为+号
longPress=driver.find_element_by_name('0')
TouchAction(driver).long_press(longPress).perform()
time.sleep(5)
assert driver.find_element_by_name('+').text in u'+'
driver.close_app()

#-----------------------------------------------------#
#            Scroll and swipe(滚动和滑动)              #
#-----------------------------------------------------#
滚动的实现案例已android自带的联系人作为测试，是java的语言，滚动的测试脚本如下：
package lession1;

/*
 * 
 * Android计数器的测试代码
 * */

import static org.testng.AssertJUnit.assertEquals;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.ios.IOSDriver;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import javax.management.DescriptorKey;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class TestApp 
{
	public AppiumDriver driver;
	
	
	@BeforeClass
	public void initalAppiumSettings()throws MalformedURLException
	{
		DesiredCapabilities cap=new DesiredCapabilities();
		
		cap.setCapability("platforName", "Android");
		//deviceName名称见:Google Nexus 10-4.4.4
//		cap.setCapability("deviceName", "Android Emulator");
//		cap.setCapability("deviceName", "Google Nexus 10-4.4.4");
		cap.setCapability("deviceName", "Samsung Galaxy S4-4.4.4");
		cap.setCapability("appActivity", "com.android.contacts.activities.PeopleActivity");
		cap.setCapability("appPackage", "com.android.contacts");
		//不重要的元素可以忽略
		cap.setCapability("ignoreUnimportantViews", "true");
		
		driver=new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), cap);
		driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	}
	
	
	
	@Test
	@DescriptorKey("webView的测试")
	public void  webView() throws InterruptedException
	{
		driver.scrollTo("Nitika");
		Thread.sleep(3000);
	}
	
	
	@AfterClass
	public void realse() throws InterruptedException
	{
//		driver.quit();
		Thread.sleep(5000);
		driver.closeApp();
	}
}


#-----------------------------------------------------#
#          Drag and drop(拖放操作,A位置到B位置)         #
#-----------------------------------------------------#
案例测试代码：
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
import time,unittest,sys,os


desired_caps={}
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['platformVersion']='4.4.4'
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='com.android.launcher'
desired_caps['appActivity']='com.android.launcher2.Launcher'
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(30)


appsIcon=driver.find_element_by_accessibility_id('Apps')
appsIcon.click()

calculator=driver.find_element_by_name('Calculator')

TouchAction(driver).press(calculator).perform()

TouchAction(driver).move_to(driver.find_element_by_accessibility_id('Widgets')).release().perform()

time.sleep(6)

driver.close_app()


#-----------------------------------------------------#
#        Pinch and zoom-->MultiAction(夹点和缩放)      #
#-----------------------------------------------------#

#-----------------------------------------------------#
#                       Alert()                       #
#-----------------------------------------------------#

#-----------------------------------------------------#
#               Capturing screenshots                 #
#-----------------------------------------------------#
为了测试报告的目的，测试失败的时候获取错误的截图。错误的截图分别为：
Byte 
Base64 
File 
见如下的测试案例代码：
from appium import  webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
import time,unittest,sys,os


desired_caps={}
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['platformVersion']='4.4.4'
desired_caps['deviceName']='Android Emulator'
desired_caps['appPackage']='com.android.launcher'
desired_caps['appActivity']='com.android.launcher2.Launcher'
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
driver.implicitly_wait(30)

driver.get_screenshot_as_file('D:/git/PyCharm/AppiumHp/file.png')
time.sleep(3)
print driver.get_screenshot_as_base64()
time.sleep(3)
print driver.get_screenshot_as_png()

driver.close_app()








