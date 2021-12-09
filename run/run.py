#coding=utf-8
import unittest
from time import strftime,sleep
import sys
sys.path.append('..')
from common.HTMLTestRunner import HTMLTestRunner
import os
import logging

#路径
case_path=os.path.abspath(os.path.join(os.getcwd(),'..'))+'\\testcase\\'
report_path=os.path.abspath(os.path.join(os.getcwd(),'..'))+'\\report\\'
log_path=os.path.abspath(os.path.join(os.getcwd(),'..'))+'\\log\\'
test_case=unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
#print(test_case)

def run_case(test_case=test_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''
    cur_time=strftime('%Y/%m/%d %H:%M:%S')
    report = reportpath +r"report.html"
    print("测试报告生成地址：%s"% report+'\n开始测试...')
    fp = open(report, "wb")
    runner = HTMLTestRunner(stream=fp, verbosity=2, title="UI自动化测试报告", description="用例执行情况")

    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_path +r"logs.log",
                        filemode='w')
    logger = logging.getLogger()
    logger.info(test_case)

    runner.run(test_case)
    fp.close()

if __name__ == "__main__":
    run_case(test_case)
