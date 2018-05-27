import xlrd
import numpy as np
import mysql.connector as myconn
import pymysql
import time, datetime
import re
import sys
import glob
import threading
import pandas as pd
import os
import xlwt

def write_to_excel(dbname):
    conn = myconn.connect(user="root", password="Jackey123456", database=dbname)
    cursor = conn.cursor()
    sql_1 = "select table_name from information_schema.tables where table_schema='%s' and table_type='base table'"
    cursor.execute(sql_1 % dbname)
    table_result = cursor.fetchall()
    table_name_arr = []
    for result in table_result:
        table_name_arr.append(result[0])

    writer = pd.ExcelWriter(dbname + ".xlsx")
    for table_name in table_name_arr:
        sql_2 = "select * from " + table_name
        cursor.execute(sql_2)
        result_set_company_info = cursor.fetchall()
        description = cursor.description
        header_names = []
        for desc in description:
            header_names.append(desc[0])
        dt = {}
        result_arr = []
        for i in range(len(header_names)):
            result_arr.append([])
        for data in result_set_company_info:
            for i in range(len(data)):
                result_arr[i].append(data[i])
        for i in range(len(header_names)):
            dt[header_names[i]] = result_arr[i]

        cols = header_names
        df = pd.DataFrame(data=dt,dtype='object')
        df = df.ix[:, cols]
        df=df.infer_objects()
        print(df.dtypes)

        df.to_excel(writer, table_name, index=False)
    writer.save()


write_to_excel("work_company")
write_to_excel("work_firm")
write_to_excel("work_fund")