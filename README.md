# UI_auto_test
这是一个基于python unittest selenium htmltestrunner写的一个UI自动化测试程序。  
bootstrap文件夹:存放着bootstrap样式，用于美化测试报告  
common文件夹:存放公共方法，如读取excel测试数据，读取config.ini配置文件，定义不同的浏览器的驱动代码  
config文件夹:配置文件，用于某些测试的场景，如交换机测试时可以将username/password/host存放在里面  
data文件夹:是一个excel文档，里面存放测试数据，(如果是xls可以使用xlrd/xlwt，xlsx需要使用openpyxl)  
driver文件夹：用于存放三种浏览器driver(chrome,ie,firefox)  
log文件夹：存放日志在logs.log中  
report文件夹：用于存放测试报告(仅支持html格式)  
run文件夹：执行测试用例(默认是导入testcase中所有的以test开头的文件)   
testcase文件夹：存放测试用例(test_01,test_02...需要自己继续写。)      
执行方法：  
首先在data中完善测试数据，然后去testcase中完善测试用例(支持ddt)，执行run.py即可，report中的报告会自动覆盖。     
