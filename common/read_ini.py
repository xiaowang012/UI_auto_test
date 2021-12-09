#coding=utf-8
import configparser

class ReadIni():
    def read():
        try:
            cf=configparser.ConfigParser()
            cf.read("config.ini")
            datas=cf.items('login')
        except:
            print('error')
        else:
            return [datas[0][1],datas[1][1],datas[2][1]]

