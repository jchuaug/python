import os
import sys
import  glob
import datetime
for filename in glob.glob(r'G:\BaiduNetdiskDownload\data\firm\*.xls'):
   print(filename)
   with open("log.txt","r") as read_file:
       name_resolved_file=read_file.read()
       if filename in name_resolved_file:
           print("文件",filename,"已被处理过，跳过")
       else:
           time_start=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           print("文件没被处理过，开始处理文件")
           with open("log.txt", "a") as write_file:
               time_end=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
               write_file.write("\n"+filename+"   Reading Start Time:"+str(time_start)+" Readind End Time:"+str(time_end))

