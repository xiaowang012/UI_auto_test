#coding=utf-8
import os
from selenium import webdriver

class CreateDriver():
    '''创建浏览器fire'''
    def create_driver(driver_name):
        driverpath=str(os.path.abspath(os.path.join(os.getcwd(), "..")))+'\\driver'
        if driver_name=='firefox':
            driverpath_firefox=driverpath+'\\geckodriver.exe'
            driver=webdriver.Firefox(executable_path=driverpath_firefox)
            return driver
        elif driver_name=='chrome':
            driverpath_chrome=driverpath+'\\chromedriver.exe'
            driver=webdriver.Chrome(executable_path=driverpath_chrome)
            return driver
        elif driver_name=='ie':
            driverpath_ie=driverpath+'\\IEDriverServer.exe'
            driver=webdriver.Ie(executable_path=driverpath_ie)
            return driver
        else:
            print('error!')  
        