#coding=utf-8
import unittest
from ddt import data,ddt,unpack
import sys 
sys.path.append("..") 
from common.read_excel import ReadExcel
from common.browser import CreateDriver
import os

#测试数据读取excel
testdatas=[]
path1=os.path.abspath(os.path.join(os.getcwd(),'..'))+'\\data\\test_data.xls'
for i in range(2,ReadExcel.get_all_rows('UI测试',path1)+1):
    data1=ReadExcel.readdata_row('UI测试',i,path1)
    data2=[]
    data2.append(data1[3])
    data2.append(data1[6])
    testdatas.append(data2)
#print(testdatas)

@ddt
class WebTest(unittest.TestCase):

    def setUp(self):
        self.dr=CreateDriver.create_driver('firefox')
        self.dr.implicitly_wait(30)
        self.dr.maximize_window()

    def tearDown(self):
        self.dr.quit()
    
    @data(*testdatas)
    @unpack
    def test_get_title(self,url,result):
        '''get_text'''
        self.dr.get(url)
        text=self.dr.title
        self.assertEqual(text,result)

if __name__=='__main__':
    unittest.main()
