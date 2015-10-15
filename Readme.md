这是使用python编写的一个完整的自动化测试框架，我先对各个目录分别的介绍下:
Data-driven:把自动化测试中使用到的数据存储在xml,csv,excel中，该目录是存储文件数据的目录
Page:这是一个package，使用了page对象设计模式，把测试中(web and app)测试的对象功能写在了这个package中
Test-report:存储自动化测试报告的目录，自动化测试报告是html的 
TestCase:自动化的测试用例，包含了web,ddt实例,app自动化测试实例的代码
seleniumGrid:seleniumGrid的测试实例代码 
allTests.py:需要执行的模块
在这些文件中，我整合了web以及app的自动化经常使用到的案例，包含了unittets,test data driver,page object
以及其他的。












