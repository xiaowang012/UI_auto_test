#coding=utf-8
import xlrd

class ReadExcel():
    
    def readdata_row(sheetname,row,path):
        '''读取指定行'''
        try:
            row=int(row)
        except:
            print('type error!')
        else:
            xls_path= path
            workbook=xlrd.open_workbook(xls_path)
            worksheet1_name = workbook.sheet_names()[0]
            sheet1=workbook.sheet_by_name(sheetname)
            row-=1
            return sheet1.row_values(row)

    def get_all_rows(sheetname,path):
        '''获取有效行数'''
        xls_path=path
        workbook=xlrd.open_workbook(xls_path)
        worksheet1_name = workbook.sheet_names()
        sheet1=workbook.sheet_by_name(sheetname)
        return sheet1.nrows


