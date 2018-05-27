#！/usr/local/bin 程序的主入口
import xlrd
import numpy as np
import mysql.connector as myconn
import pymysql
import time, datetime
import re
import sys
import  glob
import threading

sys.path.append("..")
import python3.work.date_2018_4.excel.data_resolve_fund as solution3
import python3.work.date_2018_4.excel.data_resolve_firm as solution2
import python3.work.date_2018_4.excel.data_resolve_company as solution1
# 读取文件
file_directory_firm=r'G:\BaiduNetdiskDownload\data\firm\*.xls'
file_directory_fund=r'G:\BaiduNetdiskDownload\data\fund\*.xls'
file_directory_company=r'G:\BaiduNetdiskDownload\data\company\*.xls'


def main_file_resolver(directory):
    # print("调用方法体")
    for filename in glob.glob(directory):
        # print("调用循环体")
        path=filename
        with open("log_laptop.txt", "r") as read_file:
            name_resolved_file = read_file.read()
            if path in name_resolved_file:
                print("文件", filename, "已被处理过，跳过")
            else:
                time_start = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                print("文件没被处理过，开始处理文件")
                print("***************************************当前正在处理的文件是：", path,
                      "***************************************")
                # 读取文件的头，判断是那种类型的文件
                book = xlrd.open_workbook(path)
                # 获取每个sheet的sheetname
                counts = len(book.sheets())
                if book.sheets()[0].row(0)[0].value == "Firm Overview":
                    print("excel类型为Firm Overview型的表格")
                    solution2.obtain_data(path)
                elif book.sheets()[0].row(0)[0].value == "Fund Overview":
                    print("excel类型为Fund Overview类型的表格")
                    solution3.obtain_data(path)

                else:
                    print("Excel类型为首行为公司名的类型的表格")
                    solution1.obtain_data(path)
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>处理", path, "文件结束，10s后开始处理下一文件>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
                time_end = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                time.sleep(10)
                with open("log_laptop.txt", "a") as write_file:
                    write_file.write(
                        "\n" + filename + "   Reading Start Time:" + str(time_start) + " Readind End Time:" + str(
                            time_end))
class MyThread(threading.Thread):
    def __init__(self,threadID,file_path):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.file_path=file_path
    def run(self):
        print("开始线程："+self.threadID)
        main_file_resolver(self.file_path)
        print("退出线程"+self.threadID)

#启动多线程
# print("Thread %s is running..."%threading.current_thread().name)
# # t1=MyThread('Firm Excel File Resolve Loop',file_directory_firm)
# # t2=MyThread('Fund Excel File Resolve Loop',file_directory_fund)
# # t3=MyThread('company Excel File Resolve Loop',file_directory_company)
# # t1.start()
# # t2.start()
# # t3.start()
# # t1.join()
# # t2.join()
# # t3.join()
# # print("Thread %s ended" % threading.current_thread().name)

main_file_resolver(file_directory_company)
# main_file_resolver(file_directory_firm)
main_file_resolver(file_directory_fund)