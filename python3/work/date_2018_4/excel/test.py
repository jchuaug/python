# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:28:01 2018

@author: 70365
"""

import xlwt
import pymysql
import datetime

sql = 'select * from firm_basic_info'
sheet_name = 'p_exit_'
out_path = r'G:\BaiduNetdiskDownload\output\\' + datetime.datetime.now().strftime('%Y%m%d') + '.xls'

conn = pymysql.connect(user='root', passwd='Jackey123456', db='work_firm')
cursor = conn.cursor()
count = cursor.execute(sql)
print(count)

cursor.scroll(0, mode='absolute')
results = cursor.fetchall()
fields = cursor.description
print(fields)
workbook = xlwt.Workbook()
sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)

for field in range(0, len(fields)):
    sheet.write(0, field, fields[field][0])

row = 1
col = 0
for row in range(1, len(results) + 1):
    for col in range(0, len(fields)):
        sheet.write(row, col, u'%s' % results[row - 1][col])

workbook.save(out_path)