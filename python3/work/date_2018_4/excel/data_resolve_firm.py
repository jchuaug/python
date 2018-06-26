# 第一行为Firm Overview的excel文件的处理
import pandas
import xlrd
import numpy as np
import mysql.connector as myconn
import pymysql
import time, datetime
import re

# 读取原始数据
# 获取数据库连接
conn = myconn.connect( user="root", password="fanxing123456", database="work_firm")
cursor = conn.cursor()

# 用于定位的数据关键字
index_key_firm = ['Firm Detail', 'Firm Status:', 'Firm Type:', 'Founded:', 'Cap Under Mgmt:', 'Affiliations:',
                  'Other Offices',
                  'State/Region Breakdown', 'Investment Total', 'Industry Breakdown', 'Nation Breakdown',
                  'Affiliations:',
                  'Stage Breakdown', 'Status Breakdown', 'Year Breakdown', 'Related News', 'Top Co-Investors',
                  'Direct Investments', 'Executives', 'Funds Managed By Firm']

index_key_country_name = ['Canada', 'United States', 'United States', 'United Kingdom', 'Sweden', 'Switzerland','Cayman Islands',
                          'Singapore', 'Argentina', 'Mexico', 'Italy', 'Poland', 'Romania', 'Czech Republic', 'Ukraine','Utd. Arab Em.',
                          'Colombia', 'Turkey', 'Channel Islands', 'Austria', 'Luxembourg','Russia','Taiwan','Norway',
                          'Hong Kong', 'Brazil', 'Singapore', 'Japan', 'India', 'Mauritius', 'Netherlands', 'France','Israel','Bahamas',
                          'Spain', 'Germany', 'Brazil', 'China', 'France','Australia','South Korea','Ireland','Saudi Arabia','Belgium',
                          'Denmark','Uruguay','Finland','New Zealand', 'Portugal','Hungary','Bermuda','Senegal',
                          'Thailand','Vietnam','Estonia','Lebanon','Venezuela','Vietnam','Latvia','Malta','Chile','South Africa','Jordan','Egypt',
                          'Kazakhstan','Bahrain']


# 关键字位置类
class location():
    col = 0  # 列号
    row = 0  # 行号
    index_key = ""  # 对应的关键字

    def __init__(self, row, col, index_key):
        self.col = col
        self.row = row
        self.index_key = index_key

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def get_index_key(self):
        return self.index_key


# 初始化序列
def get_col_row(index_type, sheet_data, sheet_row, sheet_col):
    # 暴力破解，遍历数据查找关键字对应行列值
    return_loc = []
    for r in range(sheet_row):
        for l in range(sheet_col):
            for index in index_type:
                if (index == sheet_data[r][l]):
                    loc = location(r, l, index)
                    return_loc.append(loc)

    return return_loc


# 信息截取，用户将传入的字符串按照指定的正则匹配截取
def info_intercept(pattern, info, info_type):
    # print("信息截取")
    pass

# 联系信息格式化，将联系信息的电话，fax和网址分块并存储
def contact_info_intercept(contact_info):
    arr = ["", "", ""]
    if len(contact_info) == 0:
        # print("Contact Info is empty")
        return arr
    else:
        result = contact_info.split("|")
        # print(result)
        if (len(result) == 3):
            arr[0] = "".join(result[0].split(": ")[1].split("-"))
            arr[1] = "".join(result[1].split(": ")[1].split("-"))
            arr[2] = result[2]
            return arr
        else:
            for r in result:
                if r.startswith("Phone"):
                    arr[0] = "".join(r.split(": ")[1].split("-"))
                elif r.startswith("Fax"):
                    arr[1] = "".join(r.split(": ")[1].split("-"))
                elif r.startswith(" Fax"):
                    arr[1] = "".join(r.split(": ")[1].split("-"))
                else:
                    arr[2] = r
            return arr


# 初始化firm信息，首次数据库信息导入和基本简单信息的导入
def initial_firm_info(dataset, loc_list, firm_name,path_file,count_sheet):
    # print("<-----------------------------------------初始化", firm_name, "的信息----------------------------------------->")
    name = firm_name
    firm_status = ""
    firm_type = ""
    funded = ""
    cap_under_mgmt = ""
    affiliations = ""
    country = ""
    state = ""
    city = ""
    detail_loc = ""
    phone = ""
    fax = ""
    website = ""
    basic_info_arr = []
    firm_id=0
    file_info=path_file+"--->"+str(count_sheet+1)
    for loc in loc_list:
        row = loc.row
        col = loc.col
        if loc.get_index_key() == "Firm Status:":
            firm_status = dataset.iloc[row][col + 1]
        elif loc.get_index_key() == "Firm Type:":
            firm_type = dataset.iloc[row][col + 1]
        elif loc.get_index_key() == "Founded:":
            funded = dataset.iloc[row][col + 1]
        elif loc.get_index_key() == "Cap Under Mgmt:":
            cap_under_mgmt = dataset.iloc[row][col + 1]
        elif loc.get_index_key() == "Affiliations:":
            affiliations = dataset.iloc[row][col + 1]
        elif loc.get_index_key()=="Firm Detail":
            # print("<-----------------------------------------更新", firm_name,
            #       "的Firm Detail的信息----------------------------------------->")
            row = loc.row + 1
            back_row = loc.row + 1
            col = loc.col
            temp_arr = []
            count = 0
            county_row = back_row
            while str(dataset.iloc[row][col]) != "nan":
                temp_arr.append(dataset.iloc[row][col])
                for county_name in index_key_country_name:
                    if county_name == dataset.iloc[row][col]:
                        county_row = county_row + count
                        break
                count = count + 1
                row = row + 1
            if county_row == 0:  # 国家名不在已知数组中
                # print(
                #     "!!!!----------------------------------------------->国家名不在已知数组中<--------------------------------------------------------!!!!")
                # print(temp_arr)
                with open("country.txt", 'a') as f:
                    f.write('\n' + "".join(temp_arr))

            else:
                flag = county_row - back_row
                if flag == 3:  # 地址有四行
                    # print("地址有四行")
                    detail_loc = detail_loc + temp_arr[0] + temp_arr[1]
                    country = temp_arr[3]
                    split_arr = temp_arr[2].split(",")  # 将州所在的行按照逗号分开
                    # print("split:", split_arr)
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        city = ",".join(split_arr[1:])
                elif flag == 2:  # 地址有三行
                    # print("地址有三行")
                    detail_loc = detail_loc + temp_arr[0]
                    country = temp_arr[2]
                    split_arr = temp_arr[1].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        for i in range(len(split_arr)):
                            if i != 0:
                                city += split_arr[i]
                elif flag == 1:  # 地址有两行
                    # print("地址有两行")
                    country = temp_arr[1]
                    split_arr = temp_arr[0].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        for i in range(len(split_arr)):
                            if i != 0:
                                city += split_arr[i]
                elif flag == 0:  # 地址有一行
                    country = temp_arr[0]
            # print("格式化地址信息前：", temp_arr)
            if len(temp_arr) == (county_row - back_row + 1):  # 没有Phone,等项
                # print("这个firm的Firm Detail信息中没有Phone,等项")
                pass


            else:
                for j in range(len(temp_arr)):
                    if j > county_row - back_row:
                        if "Phone" in temp_arr[j]:
                            p_arr = temp_arr[j].split(":")
                            phone = "".join(p_arr[1].split("-"))
                        elif "Fax" in temp_arr[j]:
                            f_arr = temp_arr[j].split(":")
                            fax = "".join(f_arr[1].split("-"))
                        else:
                            website = temp_arr[j]

            firm_detail = [detail_loc, city, state, country, phone, fax, website]
            # print("格式化地址信息后：", firm_detail)

    basic_info_arr = [name, firm_status, firm_type, funded, cap_under_mgmt, affiliations,detail_loc, city, state, country, phone, fax, website,file_info]
    # print(basic_info_arr)
    cursor.execute("select firm_id,file_info from firm_info where name=%s and funded=%s and country=%s", (firm_name,funded,country,))
    result = cursor.fetchall()
    # 数据库中没有公司信息，插入一条新的记录
    if len(result) == 0:
        # print("初次创建数据库，插入basic info的数据")
        cursor.execute(
            "insert into firm_info (name, firm_status, firm_type, funded, cap_under_mgmt, affiliations,detail_loc, city, state, country, phone, fax, website,file_info) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            basic_info_arr)
        conn.commit()
        cursor.execute("select firm_id from firm_info where name=%s and funded=%s and country=%s",(firm_name, funded, country,))
        r=cursor.fetchall()
        firm_id=r[0][0]
        return firm_id
    else:
        firm_id = result[0][0]
        path_before=result[0][1]
        # print("数据库中已有对应的firm的信息，跳过")
        if file_info in path_before:
            # print("The duplicated fund were in same sheet of same file")
            query = "update firm_info set firm_status='%s', firm_type='%s', cap_under_mgmt='%s', affiliations='%s', detail_loc='%s', city='%s', state='%s', phone='%s',website='%s' where firm_id='%s'"
            try:
                cursor.execute(query % (
                    basic_info_arr[1], basic_info_arr[2], basic_info_arr[4], basic_info_arr[5], basic_info_arr[6],
                    basic_info_arr[7], basic_info_arr[8], basic_info_arr[10], basic_info_arr[12], firm_id))
                conn.commit()
                return firm_id
            except Exception as e:
                print(e)
                conn.rollback()

        else:
            # print("数据库中已有对应的firm的信息，执行更新")
            with open('duplicated_firm.txt', 'a') as f:
                f.write(
                    '\n' + "Duplicated info:" + "|Firm Name=" + name + "| |Path Before Override=" + path_before + "" + "| |Path Now=" + file_info + "|")

            query = "update firm_info set firm_status='%s', firm_type='%s', cap_under_mgmt='%s', affiliations='%s', detail_loc='%s', city='%s', state='%s', phone='%s',website='%s',file_info='%s' where firm_id='%s'"
            # print("method_2:", query)
            try:
                cursor.execute(query % (
                    basic_info_arr[1], basic_info_arr[2], basic_info_arr[4], basic_info_arr[5], basic_info_arr[6],
                    basic_info_arr[7], basic_info_arr[8], basic_info_arr[10], basic_info_arr[12],pymysql.escape_string((path_before+" + "+basic_info_arr[13])), firm_id))
                conn.commit()
                return firm_id
            except Exception as e:
                print(e)
                conn.rollback()


# 存储firm detail信息
def formating_and_restore_firm_details(dataset, loc, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Firm Detail的信息----------------------------------------->")
    row = loc.row + 1
    back_row = loc.row + 1
    col = loc.col
    firm_name = firm_name
    country = ""
    state = ""
    city = ""
    detail_loc = ""
    phone = ""
    fax = ""
    website = ""
    temp_arr = []
    count = 0
    county_row = back_row
    while str(dataset.iloc[row][col]) != "nan":
        temp_arr.append(dataset.iloc[row][col])
        for county_name in index_key_country_name:
            if county_name == dataset.iloc[row][col]:
                county_row = county_row + count
                break
        count = count + 1
        row = row + 1
    if county_row == 0:  # 国家名不在已知数组中
        # print(
        #     "!!!!----------------------------------------------->国家名不在已知数组中<--------------------------------------------------------!!!!")
        # print(temp_arr)
        with open("country.txt", 'a') as f:
            f.write('\n' + "".join(temp_arr))

    else:
        flag = county_row - back_row
        if flag == 3:  # 地址有四行
            # print("地址有四行")
            detail_loc = detail_loc + temp_arr[0] + temp_arr[1]
            country = temp_arr[3]
            split_arr = temp_arr[2].split(",")  # 将州所在的行按照逗号分开
            # print("split:", split_arr)
            if len(split_arr) == 1:
                state = split_arr[0]
            elif len(split_arr) > 1:
                state = split_arr[0]
                city = ",".join(split_arr[1:])
        elif flag == 2:  # 地址有三行
            # print("地址有三行")
            detail_loc = detail_loc + temp_arr[0]
            country = temp_arr[2]
            split_arr = temp_arr[1].split(",")  # 将州所在的行按照逗号分开
            if len(split_arr) == 1:
                state = split_arr[0]
            elif len(split_arr) > 1:
                state = split_arr[0]
                for i in range(len(split_arr)):
                    if i != 0:
                        city += split_arr[i]
        elif flag == 1:  # 地址有两行
            # print("地址有两行")
            country = temp_arr[1]
            split_arr = temp_arr[0].split(",")  # 将州所在的行按照逗号分开
            if len(split_arr) == 1:
                state = split_arr[0]
            elif len(split_arr) > 1:
                state = split_arr[0]
                for i in range(len(split_arr)):
                    if i != 0:
                        city += split_arr[i]
        elif flag==0:#地址有一行
            country=temp_arr[0]
    # print("格式化地址信息前：", temp_arr)
    if len(temp_arr) == (county_row - back_row + 1):  # 没有Phone,等项
        # print("这个firm的Firm Detail信息中没有Phone,等项")
        pass

    else:
        for j in range(len(temp_arr)):
            if j > county_row - back_row:
                if "Phone" in temp_arr[j]:
                    p_arr = temp_arr[j].split(":")
                    phone = "".join(p_arr[1].split("-"))
                elif "Fax" in temp_arr[j]:
                    f_arr = temp_arr[j].split(":")
                    fax = "".join(f_arr[1].split("-"))
                else:
                    website = temp_arr[j]

    firm_detail = [detail_loc, city, state, country, phone, fax, website]
    # print("格式化地址信息后：", firm_detail)
    cursor.execute("select firm_id from firm_info where name=%s", (firm_name,))
    result = cursor.fetchall()
    # 数据库中没有公司信息，插入一条新的记录
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，请重新运行初始化程序")
        pass

    else:
        firm_id = result[0][0]
        # print("更新firm detail的信息")
        query = "update firm_info set detail_loc='%s', city='%s', state='%s', country='%s', phone='%s',fax='%s',website='%s' where firm_id='%s'"
        # print("method_2:", query)
        try:
            cursor.execute(query % (
                firm_detail[0], firm_detail[1], firm_detail[2], firm_detail[3], firm_detail[4], firm_detail[5],
                firm_detail[6], firm_id))
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()


# 存储Other Offices信息
def formating_and_restore_other_offices(dataset, loc, firm_id,firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Other Offices的信息----------------------------------------->")
    row = loc.row + 1
    col = loc.col
    arr = []
    firm_name = firm_name
    country = ""
    state = ""
    city = ""
    detail_loc = ""
    phone = ""
    fax = ""
    count = 0

    while True:  # 先处理左边
        # print(str(dataset.iloc[row][col]))
        country = ""
        state = ""
        city = ""
        detail_loc = ""
        phone = ""
        fax = ""
        if str(dataset.iloc[row][col]) != "nan" and dataset.iloc[row][col] == "Related News":
            break
        elif str(dataset.iloc[row][col]) == "nan" and str(dataset.iloc[row + 1][col]) !="nan" and dataset.iloc[row + 1][col]== "Related News":
            break
        elif str(dataset.iloc[row][col]) == "nan" and str(dataset.iloc[row + 1][col]) == "nan":
            row = row + 1
        elif str(dataset.iloc[row][col]) == "nan" and str(dataset.iloc[row + 1][col]) != "nan" and dataset.iloc[row + 1][col] != "Related News":
            # print("这一行为地址间的空行，跳过这一行")
            row = row + 1
        elif str(dataset.iloc[row][col]) != "nan":
            temp_arr = []
            count = 0
            county_row = row
            back_row = row
            while str(dataset.iloc[row][col]) != "nan":
                temp_arr.append(dataset.iloc[row][col])
                for county_name in index_key_country_name:
                    if county_name == dataset.iloc[row][col]:
                        county_row = county_row + count
                        break
                count = count + 1
                row = row + 1
            if county_row == back_row:  # 国家名不在已知数组中
                # print(
                #     "!!!!----------------------------------------------->国家名不在已知数组中<--------------------------------------------------------!!!!")
                # print(temp_arr)
                with open("country.txt", 'a') as f:
                    f.write('\n' + "".join(temp_arr))
                break

            else:
                flag = county_row - back_row
                if flag == 3:  # 地址有四行
                    # print("地址有四行")
                    detail_loc = detail_loc + temp_arr[0] + temp_arr[1]
                    country = temp_arr[3]
                    split_arr = temp_arr[2].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        city = ",".join(split_arr[1:])
                elif flag == 2:  # 地址有三行
                    # print("地址有三行")
                    detail_loc = temp_arr[0]
                    country = temp_arr[2]
                    split_arr = temp_arr[1].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        state = split_arr[0]
                        city = ",".join(split_arr[1:])
                elif flag == 1:  # 地址有两行
                    # print("地址有两行")
                    country = temp_arr[1]
                    split_arr = temp_arr[0].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        for i in range(len(split_arr)):
                            if i != 0:
                                city += split_arr[i]
            if len(temp_arr) == (county_row - back_row + 1):  # 没有Phone,等项
                # print("这个firm的Firm Detail信息中没有Phone,等项")
                pass

            else:
                for j in range(len(temp_arr)):
                    if j > county_row - back_row:
                        if "Phone" in str(temp_arr[j]):
                            p_arr = temp_arr[j].split(":")
                            phone = "".join(p_arr[1].split("-"))
                        elif "Fax" in str(temp_arr[j]):
                            f_arr = temp_arr[j].split(":")
                            fax = "".join(f_arr[1].split("-"))

            arr.append(["", firm_name, detail_loc, city, state, country, phone, fax])
            row = row + 1  # 一轮扫完自增1进入下一轮

    # print("左边的office录入完毕，开始录入右边的office")
    row_r = loc.row + 1
    col_r = loc.col + 1
    while True:  # 再处理右边
        country = ""
        state = ""
        city = ""
        detail_loc = ""
        phone = ""
        fax = ""
        # print(dataset.iloc[row_r][col_r], ":", dataset.iloc[row_r + 1][col_r])
        if str(dataset.iloc[row_r][col_r]) == "nan" and str(dataset.iloc[row_r + 1][col_r]) != "nan" and dataset.iloc[row_r + 1][col_r] == "Date":
            break
        if str(dataset.iloc[row_r][col_r]) == "nan" and str(dataset.iloc[row_r + 1][col_r]) != "nan" and dataset.iloc[row_r + 1][col_r] != "Date":
            row_r = row_r + 1
        if str(dataset.iloc[row_r][col_r]) == "nan" and str(dataset.iloc[row_r + 1][col_r]) == "nan":
            row_r = row_r + 1
        elif str(dataset.iloc[row_r][col_r]) == "nan" and str(dataset.iloc[row_r + 1][col_r]) != "nan":
            # print("这一行为地址间的空行，跳过这一行")
            row_r = row_r + 1
        elif str(dataset.iloc[row_r][col_r]) != "nan":
            temp_arr = []
            count = 0
            county_row = row_r
            back_row = row_r
            while str(dataset.iloc[row_r][col_r]) != "nan":
                temp_arr.append(dataset.iloc[row_r][col_r])
                for county_name in index_key_country_name:
                    if county_name == dataset.iloc[row_r][col_r]:
                        county_row = county_row + count
                        break
                count = count + 1
                row_r = row_r + 1
            if county_row == back_row:  # 国家名不在已知数组中
                # print(
                #     "!!!!----------------------------------------------->国家名不在已知数组中<--------------------------------------------------------!!!!")
                # print(temp_arr)
                with open("country.txt", 'a') as f:
                    f.write('\n' + "".join(temp_arr))
                break

            else:
                flag = county_row - back_row
                if flag == 3:  # 地址有四行
                    # print("地址有四行")
                    detail_loc = detail_loc + temp_arr[0] + temp_arr[1]
                    country = temp_arr[3]
                    split_arr = temp_arr[2].split(",")  # 将州所在的行按照逗号分开
                    # print("split:", split_arr)
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        city = ",".join(split_arr[1:])
                elif flag == 2:  # 地址有三行
                    # print("地址有三行")
                    detail_loc = detail_loc + temp_arr[0]
                    country = temp_arr[2]
                    split_arr = temp_arr[1].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        for i in range(len(split_arr)):
                            if i != 0:
                                city += split_arr[i]
                elif flag == 1:  # 地址有两行
                    # print("地址有两行")
                    country = temp_arr[1]
                    split_arr = temp_arr[0].split(",")  # 将州所在的行按照逗号分开
                    if len(split_arr) == 1:
                        state = split_arr[0]
                    elif len(split_arr) > 1:
                        state = split_arr[0]
                        for i in range(len(split_arr)):
                            if i != 0:
                                city += split_arr[i]
            if len(temp_arr) == (county_row - back_row + 1):  # 没有Phone,等项
                # print("这个firm的Firm Detail信息中没有Phone,等项")
                pass

            else:
                for j in range(len(temp_arr)):
                    if j > county_row - back_row:
                        if "Phone" in str(temp_arr[j]):
                            p_arr = temp_arr[j].split(":")
                            phone = "".join(p_arr[1].split("-"))
                        elif "Fax" in str(temp_arr[j]):
                            f_arr = temp_arr[j].split(":")
                            fax = "".join(f_arr[1].split("-"))

            arr.append(["", firm_name, detail_loc, city, state, country, phone, fax])
            row_r = row_r + 1  # 一轮扫完自增1进入下一轮

    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    cursor.execute("select other_offices_id from other_offices where firm_id=%s", (firm_id,))
    result2 = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass

    else:
        firm_id = result[0][0]
        if len(result2) == 0:
            # print("数据库中不存在输入的firm_id的other offices信息，执行插入")
            for a in arr:
                a[0] = firm_id
                cursor.execute(
                    "insert into other_offices (firm_id,firm_name,detail_loc, city, state, country, phone, fax) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

        else:
            # print("数据库中存在输入的firm_name的other offices信息，跳过")
            pass


# 格式化State/Region Breakdown下方的信息
def formating_and_restore_investment_profile_state_breakdown(dataset, loc, loc_list,firm_id, firm_name):
    # print(
    #     "<-----------------------------------------更新", firm_name,
    #     "的State/Region Breakdown的信息----------------------------------------->")
    row = loc.row + 1
    col = loc.col
    arr = []
    total_row = 0
    total_col = 0
    for loc_temp in loc_list:
        if loc_temp.get_index_key() == "Investment Total":
            total_row = loc_temp.row
            total_col = loc_temp.col + 1
            break
    num_of_company_total = "".join(str(dataset.iloc[total_row][total_col]).split(","))
    sum_inv_total = "".join(str(dataset.iloc[total_row][total_col + 1]).split(","))
    avg_per_company_total = "".join(str(dataset.iloc[total_row][total_col + 2]).split(","))
    percent_of_inv_total = "".join(str(dataset.iloc[total_row][total_col + 3]).split(","))
    state_name = ""
    num_of_company = ""
    sum_inv = ""
    avg_per_company = ""
    percent_of_inv = ""

    while str(dataset.iloc[row][col]) != "nan":
        state_name = dataset.iloc[row][col]
        num_of_company = "".join(str(dataset.iloc[row][col + 1]).split(","))
        sum_inv = "".join(str(dataset.iloc[row][col + 2]).split(","))
        avg_per_company = "".join(str(dataset.iloc[row][col + 3]).split(","))
        percent_of_inv = "".join(str(dataset.iloc[row][col + 4]).split(","))
        arr.append(["", firm_name, num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total,
                    state_name,
                    num_of_company, sum_inv, avg_per_company, percent_of_inv])
        row = row + 1

    for a in arr:
        for i in range(len(a)):
            if (a[i]) == "-":
                a[i] = ""
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:

        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute("select state_breakdown_id from state_breakdown where firm_id=%s and state_name=%s",
                           (firm_id, a[6]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的State/Region Breakdown信息，执行插入")
                cursor.execute(
                    "insert into state_breakdown (firm_id,firm_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, state_name,num_of_company, sum_inv, avg_per_company, percent_of_inv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的State/Region Breakdown信息，执行更新操作")
                query = "update state_breakdown set num_of_company_total='%s', sum_inv_total='%s', avg_per_company_total='%s', percent_of_inv_total='%s', num_of_company='%s', sum_inv='%s', avg_per_company='%s', percent_of_inv='%s' where firm_id='%s' and state_name='%s' "
                try:
                    cursor.execute(query % (a[2], a[3], a[4], a[5], a[7], a[8], a[9], a[10], firm_id, pymysql.escape_string(a[6])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Industry Breakdown下方的信息
def formating_and_restore_investment_profile_industry_breakdown(dataset, loc, loc_list,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Industry Breakdown的信息----------------------------------------->")

    row = loc.row + 1
    col = loc.col
    arr = []
    total_row = 0
    total_col = 0
    for loc_temp in loc_list:
        if loc_temp.get_index_key() == "Investment Total":
            total_row = loc_temp.row
            total_col = loc_temp.col + 1
            break
    num_of_company_total = "".join(str(dataset.iloc[total_row][total_col]).split(","))
    sum_inv_total = "".join(str(dataset.iloc[total_row][total_col + 1]).split(","))
    avg_per_company_total = "".join(str(dataset.iloc[total_row][total_col + 2]).split(","))
    percent_of_inv_total = "".join(str(dataset.iloc[total_row][total_col + 3]).split(","))
    industry_name = ""
    num_of_company = ""
    sum_inv = ""
    avg_per_company = ""
    percent_of_inv = ""

    while str(dataset.iloc[row][col]) != "nan":
        industry_name = dataset.iloc[row][col]
        num_of_company = "".join(str(dataset.iloc[row][col + 1]).split(","))
        sum_inv = "".join(str(dataset.iloc[row][col + 2]).split(","))
        avg_per_company = "".join(str(dataset.iloc[row][col + 3]).split(","))
        percent_of_inv = "".join(str(dataset.iloc[row][col + 4]).split(","))
        arr.append(["", firm_name, num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total,
                    industry_name,
                    num_of_company, sum_inv, avg_per_company, percent_of_inv])
        row = row + 1
    for a in arr:
        for i in range(len(a)):
            if (a[i]) == "-":
                a[i] = ""
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select industry_breakdown_id from industry_breakdown where firm_id=%s and industry_name=%s",
                (firm_id, a[6]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Industry Breakdown信息，执行插入")
                cursor.execute(
                    "insert into industry_breakdown (firm_id,firm_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, industry_name,num_of_company, sum_inv, avg_per_company, percent_of_inv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Industry Breakdown信息，执行更新操作")
                query = "update industry_breakdown set num_of_company_total='%s', sum_inv_total='%s', avg_per_company_total='%s', percent_of_inv_total='%s', num_of_company='%s', sum_inv='%s', avg_per_company='%s', percent_of_inv='%s' where firm_id='%s' and industry_name='%s' "
                try:
                    cursor.execute(query % (a[2], a[3], a[4], a[5], a[7], a[8], a[9], a[10], firm_id, pymysql.escape_string(a[6])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Nation Breakdown下方的信息
def formating_and_restore_investment_profile_nation_breakdown(dataset, loc, loc_list,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Nation Breakdown的信息----------------------------------------->")
    row = loc.row + 1
    col = loc.col
    arr = []
    total_row = 0
    total_col = 0
    for loc_temp in loc_list:
        if loc_temp.get_index_key() == "Investment Total":
            total_row = loc_temp.row
            total_col = loc_temp.col + 1
            break
    num_of_company_total = "".join(str(dataset.iloc[total_row][total_col]).split(","))
    sum_inv_total = "".join(str(dataset.iloc[total_row][total_col + 1]).split(","))
    avg_per_company_total = "".join(str(dataset.iloc[total_row][total_col + 2]).split(","))
    percent_of_inv_total = "".join(str(dataset.iloc[total_row][total_col + 3]).split(","))
    nation_name = ""
    num_of_company = ""
    sum_inv = ""
    avg_per_company = ""
    percent_of_inv = ""

    while str(dataset.iloc[row][col]) != "nan":
        nation_name = dataset.iloc[row][col]
        num_of_company = "".join(str(dataset.iloc[row][col + 1]).split(","))
        sum_inv = "".join(str(dataset.iloc[row][col + 2]).split(","))
        avg_per_company = "".join(str(dataset.iloc[row][col + 3]).split(","))
        percent_of_inv = "".join(str(dataset.iloc[row][col + 4]).split(","))
        arr.append(["", firm_name, num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total,
                    nation_name,
                    num_of_company, sum_inv, avg_per_company, percent_of_inv])
        row = row + 1
    for a in arr:
        for i in range(len(a)):
            if (a[i]) == "-":
                a[i] = ""
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select nation_breakdown_id from nation_breakdown where firm_id=%s and nation_name=%s",
                (firm_id, a[6]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Nation Breakdown信息，执行插入")
                cursor.execute(
                    "insert into nation_breakdown (firm_id,firm_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, nation_name,num_of_company, sum_inv, avg_per_company, percent_of_inv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Nation Breakdown信息，执行更新操作")
                query = "update nation_breakdown set num_of_company_total='%s', sum_inv_total='%s', avg_per_company_total='%s', percent_of_inv_total='%s', num_of_company='%s', sum_inv='%s', avg_per_company='%s', percent_of_inv='%s' where firm_id='%s' and nation_name='%s' "
                try:
                    cursor.execute(query % (a[2], a[3], a[4], a[5], a[7], a[8], a[9], a[10], firm_id, pymysql.escape_string(a[6])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Stage Breakdown下方的信息
def formating_and_restore_investment_profile_stage_breakdown(dataset, loc, loc_list,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Stage Breakdown的信息----------------------------------------->")
    row = loc.row + 1
    col = loc.col
    arr = []
    total_row = 0
    total_col = 0
    for loc_temp in loc_list:
        if loc_temp.get_index_key() == "Investment Total":
            total_row = loc_temp.row
            total_col = loc_temp.col + 1
            break
    num_of_company_total = "".join(str(dataset.iloc[total_row][total_col]).split(","))
    sum_inv_total = "".join(str(dataset.iloc[total_row][total_col + 1]).split(","))
    avg_per_company_total = "".join(str(dataset.iloc[total_row][total_col + 2]).split(","))
    percent_of_inv_total = "".join(str(dataset.iloc[total_row][total_col + 3]).split(","))
    stage_name = ""
    num_of_company = ""
    sum_inv = ""
    avg_per_company = ""
    percent_of_inv = ""

    while str(dataset.iloc[row][col]) != "nan":
        stage_name = dataset.iloc[row][col]
        num_of_company = "".join(str(dataset.iloc[row][col + 1]).split(","))
        sum_inv = "".join(str(dataset.iloc[row][col + 2]).split(","))
        avg_per_company = "".join(str(dataset.iloc[row][col + 3]).split(","))
        percent_of_inv = "".join(str(dataset.iloc[row][col + 4]).split(","))
        arr.append(["", firm_name, num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total,
                    stage_name,
                    num_of_company, sum_inv, avg_per_company, percent_of_inv])
        row = row + 1
    for a in arr:
        for i in range(len(a)):
            if (a[i]) == "-":
                a[i] = ""
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select stage_breakdown_id from stage_breakdown where firm_id=%s and stage_name=%s",
                (firm_id, a[6]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Stage Breakdown信息，执行插入")
                cursor.execute(
                    "insert into stage_breakdown (firm_id,firm_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, stage_name,num_of_company, sum_inv, avg_per_company, percent_of_inv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Stage Breakdown信息，执行更新操作")
                query = "update stage_breakdown set num_of_company_total='%s', sum_inv_total='%s', avg_per_company_total='%s', percent_of_inv_total='%s', num_of_company='%s', sum_inv='%s', avg_per_company='%s', percent_of_inv='%s' where firm_id='%s' and stage_name='%s' "
                try:
                    cursor.execute(query % (a[2], a[3], a[4], a[5], a[7], a[8], a[9], a[10], firm_id, pymysql.escape_string(a[6])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Status Breakdown下方的信息
def formating_and_restore_investment_profile_status_breakdown(dataset, loc, loc_list,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Status Breakdown的信息----------------------------------------->")
    row = loc.row + 1
    col = loc.col
    arr = []
    total_row = 0
    total_col = 0
    for loc_temp in loc_list:
        if loc_temp.get_index_key() == "Investment Total":
            total_row = loc_temp.row
            total_col = loc_temp.col + 1
            break
    num_of_company_total = "".join(str(dataset.iloc[total_row][total_col]).split(","))
    sum_inv_total = "".join(str(dataset.iloc[total_row][total_col + 1]).split(","))
    avg_per_company_total = "".join(str(dataset.iloc[total_row][total_col + 2]).split(","))
    percent_of_inv_total = "".join(str(dataset.iloc[total_row][total_col + 3]).split(","))
    status_name = ""
    num_of_company = ""
    sum_inv = ""
    avg_per_company = ""
    percent_of_inv = ""

    while str(dataset.iloc[row][col]) != "nan":
        status_name = dataset.iloc[row][col]
        num_of_company = "".join(str(dataset.iloc[row][col + 1]).split(","))
        sum_inv = "".join(str(dataset.iloc[row][col + 2]).split(","))
        avg_per_company = "".join(str(dataset.iloc[row][col + 3]).split(","))
        percent_of_inv = "".join(str(dataset.iloc[row][col + 4]).split(","))
        arr.append(["", firm_name, num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total,
                    status_name,
                    num_of_company, sum_inv, avg_per_company, percent_of_inv])
        row = row + 1
    for a in arr:
        for i in range(len(a)):
            if (a[i]) == "-":
                a[i] = ""
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select status_breakdown_id from status_breakdown where firm_id=%s and status_name=%s",
                (firm_id, a[6]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Status Breakdown信息，执行插入")
                cursor.execute(
                    "insert into status_breakdown (firm_id,firm_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, status_name,num_of_company, sum_inv, avg_per_company, percent_of_inv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Status Breakdown信息，执行更新操作")
                query = "update status_breakdown set num_of_company_total='%s', sum_inv_total='%s', avg_per_company_total='%s', percent_of_inv_total='%s', num_of_company='%s', sum_inv='%s', avg_per_company='%s', percent_of_inv='%s' where firm_id='%s' and status_name='%s' "
                try:
                    cursor.execute(query % (a[2], a[3], a[4], a[5], a[7], a[8], a[9], a[10], firm_id, pymysql.escape_string(a[6])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Year Breakdown下方的信息
def formating_and_restore_investment_profile_year_breakdown(dataset, loc, loc_list,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Year Breakdown的信息----------------------------------------->")
    row = loc.row + 1
    col = loc.col
    arr = []
    total_row = 0
    total_col = 0
    for loc_temp in loc_list:
        if loc_temp.get_index_key() == "Investment Total":
            total_row = loc_temp.row
            total_col = loc_temp.col + 1
            break
    num_of_company_total = "".join(str(dataset.iloc[total_row][total_col]).split(","))
    sum_inv_total = "".join(str(dataset.iloc[total_row][total_col + 1]).split(","))
    avg_per_company_total = "".join(str(dataset.iloc[total_row][total_col + 2]).split(","))
    percent_of_inv_total = "".join(str(dataset.iloc[total_row][total_col + 3]).split(","))
    year_name = ""
    num_of_company = ""
    sum_inv = ""
    avg_per_company = ""
    percent_of_inv = ""

    while str(dataset.iloc[row][col]) != "nan":
        year_name = dataset.iloc[row][col]
        num_of_company = "".join(str(dataset.iloc[row][col + 1]).split(","))
        sum_inv = "".join(str(dataset.iloc[row][col + 2]).split(","))
        avg_per_company ="".join( str(dataset.iloc[row][col + 3]).split(","))
        percent_of_inv = "".join(str(dataset.iloc[row][col + 4]).split(","))
        arr.append(
            ["", firm_name, num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, year_name,
             num_of_company, sum_inv, avg_per_company, percent_of_inv])
        row = row + 1
    for a in arr:
        for i in range(len(a)):
            if(a[i])=="-":
                a[i]=""
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select year_breakdown_id from year_breakdown where firm_id=%s and year_name=%s",
                (firm_id, a[6]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Year Breakdown信息，执行插入")
                cursor.execute(
                    "insert into year_breakdown (firm_id,firm_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, year_name,num_of_company, sum_inv, avg_per_company, percent_of_inv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Year Breakdown信息，执行更新操作")
                query = "update year_breakdown set num_of_company_total='%s', sum_inv_total='%s', avg_per_company_total='%s', percent_of_inv_total='%s', num_of_company='%s', sum_inv='%s', avg_per_company='%s', percent_of_inv='%s' where firm_id='%s' and year_name='%s' "
                try:
                    cursor.execute(query % (a[2], a[3], a[4], a[5], a[7], a[8], a[9], a[10], firm_id, a[6]))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Top Co-Investors下方的信息
def formating_and_restore_top_co_investors(dataset, loc, firm_id,firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Top Co-Investors的信息----------------------------------------->")
    row = loc.row + 2
    col = loc.col
    arr = []
    name = ""
    num_of_companies = ""
    num_of_rounds = ""
    while str(dataset.iloc[row][col]) != "nan":
        name = dataset.iloc[row][col]
        num_of_companies = dataset.iloc[row][col + 1]
        num_of_rounds = dataset.iloc[row][col + 2]
        arr.append(["", firm_name, name, num_of_companies, num_of_rounds])
        row = row + 1
    for a in arr:
        pass
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select top_coinvestors_id from top_coinvestors where firm_id=%s and name=%s",
                (firm_id, a[2]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Top Co-Investors信息，执行插入")
                cursor.execute(
                    "insert into top_coinvestors (firm_id,firm_name,name, num_of_companies, num_of_rounds) values(%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Top Co-Investors信息，执行更新操作")
                query = "update top_coinvestors set num_of_companies='%s', num_of_rounds='%s' where firm_id='%s' and name='%s' "
                try:
                    cursor.execute(query % (a[3], a[4], firm_id, pymysql.escape_string(a[2])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Related News下方的信息
def formating_and_restore_related_news(dataset, loc,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Related News的信息----------------------------------------->")
    row = loc.row + 2
    col = loc.col
    arr = []
    headline = ""
    date = ""
    publication = ""
    while str(dataset.iloc[row][col]) != "nan":
        headline = dataset.iloc[row][col]
        date = dataset.iloc[row][col + 1]
        publication = dataset.iloc[row][col + 2]
        arr.append(["", firm_name, headline, date, publication])
        row = row + 1
    for a in arr:
        pass
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select related_news_id from related_news where firm_id=%s and headline=%s",
                (firm_id, a[2]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Related News信息，执行插入")
                cursor.execute(
                    "insert into related_news (firm_id,firm_name,headline, date, publication) values(%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Related News信息，执行更新操作")
                query = "update related_news set date='%s', publication='%s' where firm_id='%s' and headline='%s' "
                try:
                    cursor.execute(query % (a[3], pymysql.escape_string(a[4]), firm_id, pymysql.escape_string(a[2])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Direct Investments下方的信息
def formating_and_restore_direct_investments(dataset, loc,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Direct Investments的信息----------------------------------------->")
    row = loc.row + 2
    col = loc.col
    arr = []
    company_name = ""
    industry = ""
    still_in_portfolio = ""
    company_status = ""
    last_investment_date = ""
    location = ""
    while str(dataset.iloc[row][col]) != "nan":
        company_name = dataset.iloc[row][col]
        industry = dataset.iloc[row][col + 1]
        still_in_portfolio = dataset.iloc[row][col + 2]
        company_status = dataset.iloc[row][col + 3]
        last_investment_date = dataset.iloc[row][col + 4]
        location = dataset.iloc[row][col + 5]
        arr.append(
            ["", firm_name, company_name, industry, still_in_portfolio, company_status, last_investment_date, location])
        row = row + 1
    for a in arr:
        pass
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            for i in range(len(a)):
                if str(a[i])=="nan":
                    a[i]=""
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select direct_investments_id from direct_investments where firm_id=%s and company_name=%s",
                (firm_id, a[2]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Direct Investments信息，执行插入")
                cursor.execute(
                    "insert into direct_investments (firm_id,firm_name,company_name, industry, still_in_portfolio, company_status, last_investment_date, location) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Direct Investments信息，执行更新操作")
                query = "update direct_investments set industry='%s', still_in_portfolio='%s',company_status='%s',last_investment_date='%s',location='%s' where firm_id='%s' and company_name='%s' "
                try:
                    cursor.execute(query % (pymysql.escape_string(a[3]), a[4], pymysql.escape_string(a[5]), a[6], pymysql.escape_string(a[7]), firm_id, pymysql.escape_string(a[2])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Funds Managed By Firm下方的信息
def formating_and_restore_funds_managed_by_firm(dataset, loc,firm_id, firm_name):
    # print(
    #     "<-----------------------------------------更新", firm_name,
    #     "的Funds Managed By Firm的信息----------------------------------------->")
    row = loc.row + 2
    col = loc.col
    arr = []
    name = ""
    size = ""
    fund_stage = ""
    vintage = ""
    while str(dataset.iloc[row][col]) != "nan":
        name = dataset.iloc[row][col]
        size = dataset.iloc[row][col + 1]
        if str(dataset.iloc[row][col + 2])=="nan":
            fund_stage=""
        else:
            fund_stage = dataset.iloc[row][col + 2]
        vintage = dataset.iloc[row][col + 3]
        arr.append(["", firm_name, name, size, fund_stage, vintage])
        row = row + 1
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select funds_managed_id from funds_managed where firm_id=%s and name=%s",
                (firm_id, a[2]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Funds Managed By Firm信息，执行插入")
                cursor.execute(
                    "insert into funds_managed (firm_id,firm_name,name, size, fund_stage, vintage) values(%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Funds Managed By Firm信息，执行更新操作")
                query = "update funds_managed set size='%s', fund_stage='%s',vintage='%s' where firm_id='%s' and name='%s' "
                try:
                    cursor.execute(query % (a[3], pymysql.escape_string(a[4]), a[5], firm_id, pymysql.escape_string(a[2])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


# 格式化Executives下方的信息
def formating_and_restore_executives(dataset, loc,firm_id, firm_name):
    # print("<-----------------------------------------更新", firm_name,
    #       "的Executives的信息----------------------------------------->")

    row = loc.row + 2
    col = loc.col
    arr = []
    name = ""
    title = ""
    phone = ""
    email = ""
    while str(dataset.iloc[row][col]) != "nan":
        name = dataset.iloc[row][col]
        title = dataset.iloc[row][col + 1]
        phone = dataset.iloc[row][col + 2]
        email = dataset.iloc[row][col + 3]
        arr.append(["", firm_name, name, title, phone, email])
        row = row + 1
    cursor.execute("select firm_id from firm_info where firm_id=%s", (firm_id,))
    result = cursor.fetchall()
    # 数据库中没有firm信息，插入不成功
    if len(result) == 0:
        # print("数据库中不存在输入的firm_name信息，插入不成功")
        pass
    else:
        for a in arr:
            firm_id = result[0][0]
            a[0] = firm_id
            cursor.execute(
                "select executives_id from executives where firm_id=%s and name=%s",
                (firm_id, a[2]))
            result2 = cursor.fetchall()
            if len(result2) == 0:
                # print("数据库中不存在输入的", firm_name, "的Executives信息，执行插入")
                cursor.execute(
                    "insert into executives (firm_id,firm_name,name, title, phone, email) values(%s,%s,%s,%s,%s,%s)",
                    a)
                conn.commit()

            else:
                # print("数据库中存在输入的", firm_name, "的Executives信息，执行更新操作")
                query = "update executives set title='%s', phone='%s',email='%s' where firm_id='%s' and name='%s' "
                try:
                    cursor.execute(query % (pymysql.escape_string(a[3]), a[4], a[5], firm_id, pymysql.escape_string(a[2])))
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()


def obtain_data(path):
    book = xlrd.open_workbook(path)
    # 获取每个sheet的sheetname
    counts = len(book.sheets())
    conn = myconn.connect( user="root", password="fanxing123456", database="work_firm")
    cursor = conn.cursor()

    for count in range(counts):
        origin_data = pandas.read_excel(path, sheet_name=count)
        if (origin_data.__len__() != 0):
            # 行数
            cols = len(origin_data.iloc[0, :])
            # 列数
            rows = len(origin_data.iloc[:, 0])
            # 将原始数据转成矩阵
            data = origin_data.as_matrix()
            # 获取行列数据集
            location_list = get_col_row(index_key_firm, data, rows, cols)
            # 建立关键字索引
            print("开始检索%s的第%d张sheet" % (path,count + 1))
            # 建立数据库
            # print("执行第%d张sheet的数据到数据库" % (count + 1))
            firm_name = origin_data.iloc[1, 0]
            print("写入%s的数据到数据库......"%(firm_name))
            # 初始化
            firm_id = initial_firm_info(origin_data, location_list, firm_name,path,count)
            # print("initialed result:", firm_id)

            for loc in location_list:
                if loc.get_index_key() == "State/Region Breakdown":
                    formating_and_restore_investment_profile_state_breakdown(origin_data, loc, location_list, firm_id,
                                                                             firm_name)
                elif loc.get_index_key() == "Industry Breakdown":
                    formating_and_restore_investment_profile_industry_breakdown(origin_data, loc, location_list,
                                                                                firm_id, firm_name)
                elif loc.get_index_key() == "Nation Breakdown":
                    formating_and_restore_investment_profile_nation_breakdown(origin_data, loc, location_list, firm_id,
                                                                              firm_name)
                elif loc.get_index_key() == "Stage Breakdown":
                    formating_and_restore_investment_profile_stage_breakdown(origin_data, loc, location_list, firm_id,
                                                                             firm_name)
                elif loc.get_index_key() == "Status Breakdown":
                    formating_and_restore_investment_profile_status_breakdown(origin_data, loc, location_list, firm_id,
                                                                              firm_name)
                elif loc.get_index_key() == "Year Breakdown":
                    formating_and_restore_investment_profile_year_breakdown(origin_data, loc, location_list, firm_id,
                                                                            firm_name)
                elif loc.get_index_key() == "Other Offices":
                    formating_and_restore_other_offices(origin_data, loc, firm_id, firm_name)
                elif loc.get_index_key() == "Related News":
                    formating_and_restore_related_news(origin_data, loc, firm_id, firm_name)
                elif loc.get_index_key() == "Top Co-Investors":
                    formating_and_restore_top_co_investors(origin_data, loc, firm_id, firm_name)
                elif loc.get_index_key() == "Direct Investments":
                    formating_and_restore_direct_investments(origin_data, loc, firm_id, firm_name)
                elif loc.get_index_key() == "Executives":
                    formating_and_restore_executives(origin_data, loc, firm_id, firm_name)
                elif loc.get_index_key() == "Funds Managed By Firm":
                    formating_and_restore_funds_managed_by_firm(origin_data, loc, firm_id, firm_name)
                else:
                    # print("！！关键字", loc.get_index_key(), "对应的处理还未实现！！")
                    pass
        else:
            print("第%d张sheet中没有数据" % (count + 1))
            continue
    print(path + "所有子表的数据导入结束")
    conn.close()
