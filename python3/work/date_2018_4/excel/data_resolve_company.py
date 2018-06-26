# 第一行为公司名的excel文件的处理
import pandas
import xlrd
import numpy as np
import mysql.connector as myconn
import pymysql
import time, datetime
import re

# 获取数据库连接
conn = myconn.connect( user="root", password="fanxing123456", database="work_company")
cursor = conn.cursor()

# 用于定位的数据关键字
index_key_firm = ['SIC Code', 'NAIC', 'Business Description', 'Alias(es)', 'Company Founded Date', 'Company Status',
                  'Current Operating Stage', 'PE Backed Status', 'Total Funding to Date', 'Investment Rounds',
                  'Mergers and Acquisitions', '# of Employees', 'Company Directors', 'Assets', 'Income Statement',
                  'Current Private Equity Investors', 'Liabilities', 'Key Financials',
                  'Historical Private Equity Investors', 'Products', 'Company Officers', 'Current Operating Stage',
                  'Legal Counsel', 'Accountant', 'Post IPO Information', '   Ticker', '   Exchange', '   IPO Date',
                  '   Amount Mil', '   Proceeds', '   Book Manager(s)', 'Last Available Sales Figure','VE Industry Code']


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

def address_split(address):
    # print("整理地址")
    detail_loc=""
    city=""
    state=""
    code=""
    country=""
    arr_address=str(address).split(",")
    if len(arr_address)==3:
        detail_loc = arr_address[0]
        city = arr_address[1]
        code = re.sub("\D", "", arr_address[2])
        if code=="":
            country=arr_address[2]
        else:
            if len(arr_address[2].split(code))==2:
                state=arr_address[2].split(code)[0]
                country=arr_address[2].split(code)[1]
            else:
                country = arr_address[2].split(code)[0]
    elif len(arr_address)==2:
        detail_loc=arr_address[0]
        code=re.sub("\D", "", arr_address[1])
        if code=="":
            country=arr_address[1]
        else:
            if len( arr_address[1].split(code))==2:
                state = arr_address[1].split(code)[0]
                country = arr_address[1].split(code)[1]
            else:
                country = arr_address[1].split(code)[0]

    elif len(arr_address)==1:
        code = re.sub("\D", "", arr_address[0])
        if code=="":
            country = arr_address[0]
        else:
            if len(arr_address[0].split(code))==2:
                state = arr_address[0].split(code)[0]
                country = arr_address[0].split(code)[1]
            else:
                country = arr_address[0].split(code)[0]


    result=[country,state,code,city,detail_loc]
    # print(result)
    return  result

def init_company_info(dataset,location_list,company_name):
    print("初始化数据")
    address_detail=""
    address_city=""
    address_state=""
    address_country=""
    address_code=""
    phone=""
    fax=""
    website=""
    ve_industry_code=""
    sic_code=""
    naic=""
    alias=""
    found_date=""
    found_year=""
    found_month=""
    found_day=""
    company_status=""
    current_operating_stage=""
    pe_backed_status=""
    total_funding_to_date=""
    bussiness_description=""
    basic_info=[]
    address=dataset.iloc[0][0]
    address_return=address_split(address)
    address_country=address_return[0]
    address_state=address_return[1]
    address_code=address_return[2]
    address_city=address_return[3]
    address_detail=address_return[4]

    contact_str=dataset.iloc[1][0]
    print(contact_str)
    contact_arr=contact_info_intercept(contact_str)
    print(contact_arr)
    phone=contact_arr[0]
    fax=contact_arr[1]
    website=contact_arr[2]
    for loc in location_list:
        row=loc.row
        col=loc.col
        if loc.get_index_key()=="VE Industry Code":
            if str(dataset.iloc[row][col + 1]) != "nan":
                ve_industry_code=dataset.iloc[row][col+1]
                print("ve_industry_code:",ve_industry_code)
        elif loc.get_index_key()=="SIC Code":
            if str(dataset.iloc[row][col + 1]) != "nan":
                sic_code=dataset.iloc[row][col+1]
        elif loc.get_index_key() == "NAIC":
            if str(dataset.iloc[row][col + 1]) != "nan":
                naic=dataset.iloc[row][col+1]
        elif loc.get_index_key() == "Alias(es)":
            if str(dataset.iloc[row][col + 1]) != "nan":
                alias=dataset.iloc[row][col + 1]
        elif loc.get_index_key() == "Company Founded Date":
            found_date=dataset.iloc[row][col+1]
            if str(found_date)=="nan":
                continue
            else:
                temp_arr=found_date.split("/")
                found_year=temp_arr[2]
                found_month=temp_arr[1]
                found_day=temp_arr[0]
        elif loc.get_index_key() == "Business Description":
            if str(dataset.iloc[row+1][col]) != "nan":
                bussiness_description=dataset.iloc[row+1][col]
        elif loc.get_index_key() == "Company Status":
            if str(dataset.iloc[row][col + 1]) != "nan":
                company_status=str(dataset.iloc[row][col+1])
        elif loc.get_index_key() == "Current Operating Stage":
            if str(dataset.iloc[row][col + 1]) != "nan":
                current_operating_stage=dataset.iloc[row][col+1]
        elif loc.get_index_key() == "PE Backed Status":
            if str(dataset.iloc[row][col+1])!="nan":
                pe_backed_status =dataset.iloc[row][col+1]
        elif loc.get_index_key() == "Total Funding to Date":
            if str(dataset.iloc[row][col + 1]) != "nan":
                total_funding_to_date=dataset.iloc[row][col+1]
    init_arr=[company_name,address_country,address_state,address_city,address_detail,address_code,phone,fax,website,ve_industry_code,sic_code,naic,bussiness_description,found_date,found_year,found_month,found_day,alias,company_status,pe_backed_status,current_operating_stage,total_funding_to_date]
    print(init_arr)
    return  init_arr



# 更新数据，简单更新方式一，即：数据唯一而且数据位置在关键字位置右边,且要更新的数据类类型为str
def update_info_simple_1_str(dataset, location_value, tablename, table_item_name, company_id):

    data_to_be_updated = dataset.iloc[location_value.row, location_value.col + 1]
    # print("update_info_simple_1_str" + table_item_name+str(data_to_be_updated))
    # cursor = conn.cursor()
    query = "update " + tablename + " set " + table_item_name + "='%s' where company_id='%s'"
    try:
        cursor.execute(query % (pymysql.escape_string(str(data_to_be_updated)), company_id))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


# 更新数据，简单更新方式二，即：数据唯一而且数据位置在关键字位置右边,且要更新的数据类型为int
def update_info_simple_1_int(dataset, location_value, tablename, table_item_name, company_id):
    # print("update_info_simple_1_int"+table_item_name)
    data_to_be_updated = dataset.iloc[location_value.row, location_value.col + 1]
    # cursor = conn.cursor()
    query = "update " + tablename + " set " + table_item_name + "='%s' where company_id='%s'"
    try:
        cursor.execute(query % (data_to_be_updated, company_id))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


# 更新数据，简单更新方式三，即：数据唯一而且数据位置在关键字位置下面,且数据类型为str
def update_info_simple_2_str(dataset, location_value, tablename, table_item_name, company_id):
    # print("update_info_simple_2_str" + table_item_name)
    data_to_be_updated = dataset.iloc[location_value.row + 1, location_value.col]
    # cursor = conn.cursor()
    query = "update " + tablename + " set " + table_item_name + "='%s' where company_id='%s'"
    try:
        cursor.execute(query % (pymysql.escape_string(data_to_be_updated), company_id))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


# 更新数据，简单更新方式四，即：数据唯一而且数据位置在关键字位置下面,且数据为超长文本
def update_info_simple_2_longstr(dataset, location_value, tablename, table_item_name, company_id):
    # print("update_info_simple_2_longstr" + table_item_name)
    data_to_be_updated = dataset.iloc[location_value.row + 1, location_value.col]
    # cursor = conn.cursor()
    query = "update " + tablename + " set " + table_item_name + "='%s' where company_id='%s'"
    try:
        cursor.execute(query % (pymysql.escape_string(data_to_be_updated), company_id))
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()


# 更新数据，复杂更新方式一，即：数更新Investment Rounds下方的数据
def update_info_complex_inv_rounds(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,"下方的数据插入操作-------------------------------------------------------")
    arr = []  # date,stage,num_of_inv,deal_value,equity_amount
    date = ""
    num_of_inv = ""
    stage = ""
    deal_value = ""
    equity_amount = ""
    pe_debt_amt = ""
    company_valuation = ""
    investment_location = ""
    firm = ""
    fund = ""
    fund_security_type = ""
    p_equity_amount = ""
    debt = ""
    # 关键字的起始位置
    row = location_value.row + 2
    col = location_value.col
    while (str(dataset.iloc[row, col]) == "nan") or (
            re.match(r"\d{2}/\d{2}/\d{4}", str(dataset.iloc[row, col])) != None):
        if re.match(r"\d{2}/\d{2}/\d{4}", str(dataset.iloc[row, col])):
            date = dataset.iloc[row, col]
            num_of_inv = dataset.iloc[row, col + 2]
            stage = dataset.iloc[row, col + 1]
            deal_value = str(dataset.iloc[row, col + 3])
            equity_amount = dataset.iloc[row, col + 4]
            pe_debt_amt = dataset.iloc[row, col + 5]
            company_valuation = dataset.iloc[row, col + 6]
            investment_location = dataset.iloc[row, col + 7]
        elif str(dataset.iloc[row, col]) == "nan" and str(dataset.iloc[row, col + 1]) == "Firm":
            row = row + 1
            continue
        else:
            firm = dataset.iloc[row, col + 1]
            fund = dataset.iloc[row, col + 2]
            p_equity_amount = dataset.iloc[row, col + 4]
            debt = dataset.iloc[row, col + 5]
            if fund != "":
                fund_security_type = dataset.iloc[row, col + 3]
            arr.append(
                [company_id, company_name, date, num_of_inv, stage, deal_value, equity_amount, pe_debt_amt,
                 company_valuation,
                 investment_location, firm, fund, fund_security_type, p_equity_amount, debt])
        row = row + 1
    for a in arr:
        for x in range(len(a)):
            if str(a[x]) == "nan" and (x == 13 or x == 14):
                a[x] = ''
            elif str(a[x]) == "nan":
                a[x] = ""
            elif a[x] == "-":
                a[x] = ''
            elif re.match(r'[0-9]+.[0-9]+\(e\)', str(a[x])):
                a[x] = "".join(("".join(a[x].split("("))).split(")"))
    for a in arr:
        for x in range(len(a)):
            if x == 5:
                a[x] = "".join(a[x].split(","))

    for a in arr:
        # 插入数据库操作
        cursor.execute("select investment_rounds_id from investment_rounds where (firm=%s and fund=%s and date=%s)",
                       (a[10], a[11], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into investment_rounds (company_id, company_name, date, num_of_inv, stage, deal_value, equity_amount, pe_debt_amt, company_valuation,investment_location, firm, fund, fund_security_type,p_equity_amount, debt) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:
            query = "update investment_rounds set num_of_inv='%s', stage='%s', deal_value='%s', equity_amount='%s', pe_debt_amt='%s', company_valuation='%s',investment_location='%s', fund_security_type='%s',p_equity_amount='%s', debt='%s' where (firm='%s' and fund='%s' and date='%s')"
            try:
                cursor.execute(
                    query % (
                    a[3], a[4], a[5], a[6], a[7], a[8], pymysql.escape_string(a[9]), a[12], a[13], a[14], pymysql.escape_string(a[10]), pymysql.escape_string(a[11]),
                    pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)

                conn.rollback()


# 更新数据，复杂更新方式二，即：数更新Mergers and Acquisitions下方的数据
def update_info_complex_merges_and_acquisitions(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    # 关键字的起始位置
    row = location_value.row + 2
    col = location_value.col
    date = ""
    target_name = ""
    acquiror_name = ""
    status = ""
    deal_value = ""
    ev_ebitda = ""
    target_financial_advisor = ""
    brief_desciption = ""
    while re.match(r"\d{2}/\d{2}/\d{4}", str(dataset.iloc[row, col])) != None:
        date = dataset.iloc[row, col]
        target_name = dataset.iloc[row, col + 1]
        acquiror_name = dataset.iloc[row, col + 2]
        status = dataset.iloc[row, col + 3]
        deal_value = dataset.iloc[row, col + 4]
        ev_ebitda = dataset.iloc[row, col + 5]
        target_financial_advisor = dataset.iloc[row, col + 6]
        brief_desciption = dataset.iloc[row + 1, col]
        arr.append([company_id, company_name, date, target_name, acquiror_name, status, deal_value, ev_ebitda,
                    target_financial_advisor,
                    brief_desciption])
        row = row + 2
    # 查询处理后的结果
    for a in arr:
        for x in range(len(a)):
            if a[x] == "-" and x == 6:
                a[x] = ""
            if str(a[x]) == "nan" and x == 6:
                a[x] = ""
            elif str(a[x]) == "nan":
                a[x] = ""
            elif a[x] == "-":
                a[x] = ""
    # 插入数据库操作
    for a in arr:
        # 插入数据库操作
        cursor.execute(
            "select mergers_acquisitions_id from mergers_acquisitions where (target_name=%s and acquiror_name=%s and date=%s)",
            (a[3], a[4], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into mergers_acquisitions (company_id,company_name,date, target_name, acquiror_name, status, deal_value, ev_ebitda, target_financial_advisor,brief_desciption) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:
            query = "update mergers_acquisitions set status='%s', deal_value='%s', ev_ebitda='%s', target_financial_advisor='%s', brief_desciption='%s' where (target_name='%s' and acquiror_name='%s' and date='%s')"

            try:
                cursor.execute(query % (
                a[5], a[6], [7], pymysql.escape_string(a[8]), pymysql.escape_string(a[9]), pymysql.escape_string(a[3]),
                pymysql.escape_string(a[4]), pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式三，即：更新Current Private Equity Investors下方的数据
def update_info_complex_curren_private_equity_investors(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    arr_round = []
    # 关键字的起始位置
    row = location_value.row + 2
    col = location_value.col
    firm = ""
    fund = ""
    fund_stage = ""
    participation_round = []
    while str(dataset.iloc[row, col]) != "nan":
        firm = dataset.iloc[row, col]
        fund = dataset.iloc[row, col + 1]
        fund_stage = dataset.iloc[row, col + 2]
        participation_round = str(dataset.iloc[row, col + 3]).split(",")
        arr.append([company_id, company_name, firm, fund, fund_stage])
        arr_round.append(participation_round)
        row = row + 1  # 向下一行检索
    # 检索结束，输出检索结果
    rounds = []
    for a, r in zip(arr, arr_round):
        rounds_item = ["", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0,0, 0, 0, 0, 0]
        for i in range(len(r)):
            rounds_item[int(r[i]) + 3] = 1
        rounds_item[0] = a[0]
        rounds_item[1] = a[1]
        rounds_item[2] = a[2]
        rounds_item[3] = a[3]
        rounds.append(rounds_item)
    for r in rounds:
        cursor.execute(
            "select participation_round_id from participation_round  where company_id=%s and firm=%s and fund=%s",
            (r[0], r[2], r[3],))
        result2 = cursor.fetchall()
        # 数据库中数据不存在
        if len(result2) == 0:
            cursor.execute(
                "insert into participation_round (company_id,company_name,firm, fund, round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11,round12,round13,round14,round15,round16,round17,round18,round19,round20,round21,round22,round23,round24,round25,round26,round27,round28,round29,round30,round31,round32,round33,round34,round35,round36,round37,round38,round39,round40,round41,round42,round43,round44,round45,round46,round47,round48,round49,round50) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                r)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()

        else:

            query = "update participation_round set round1='%s',round2='%s',round3='%s',round4='%s',round5='%s',round6='%s',round7='%s',round8='%s',round9='%s',round10='%s',round11='%s',round12='%s',round13='%s',round14='%s',round15='%s',round16='%s',round17='%s',round18='%s',round19='%s',round20='%s',round21='%s',round22='%s',round23='%s',round24='%s',round25='%s' ,round26='%s',round27='%s',round28='%s',round29='%s',round30='%s',round31='%s',round32='%s',round33='%s',round34='%s',round35='%s',round36='%s',round37='%s',round38='%s',round39='%s',round40='%s',round41='%s',round42='%s',round43='%s',round44='%s',round45='%s',round46='%s',round47='%s',round48='%s',round49='%s',round50='%s' where (company_id='%s' and firm='%s' and fund='%s')"

            try:
                cursor.execute(query % (
                    r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18],
                    r[19], r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27], r[28],r[29], r[30], r[31], r[32], r[33],
                    r[34], r[35], r[36], r[37], r[38],r[39], r[40], r[41], r[42], r[43],r[44], r[45], r[46], r[47], r[48],
                    r[49], r[50], r[51], r[52], r[53],
                    r[0], pymysql.escape_string(r[2]), pymysql.escape_string(r[3])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
    for a in arr:
        # 插入数据库操作
        cursor.execute(
            "select current_investors_id from current_investors where (company_id=%s and firm=%s and fund=%s)",
            (a[0], a[2], a[3],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into current_investors (company_id,company_name,firm, fund, fund_stage) values(%s,%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
            cursor.execute(
                "select participation_round_id from participation_round  where company_id=%s and firm=%s and fund=%s",
                (r[0], r[2], r[3],))
            result3 = cursor.fetchall()
            participation_round_id = result3[0][0]
            query = "update current_investors set participation_round_id='%s' where (company_id='%s' and firm='%s' and fund='%s')"

            try:
                cursor.execute(
                    query % (participation_round_id, a[0], pymysql.escape_string(a[2]), pymysql.escape_string(a[3])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        else:

            query = "update current_investors set fund_stage='%s' where (company_id='%s' and firm='%s' and fund='%s')"

            try:
                cursor.execute(query % (a[4], a[0], pymysql.escape_string(a[2]), pymysql.escape_string(a[3])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式四，即：更新Historical Private Equity Investors下方的数据
def update_info_complex_historical_private_investors(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    round_arr = []
    # 关键字的起始位置

    row = location_value.row + 3
    col = location_value.col
    firm = ""
    fund = ""
    fund_stage = ""
    still_in_portfolio = ""
    participation_round = []
    while str(dataset.iloc[row, col]) != "nan":
        firm = dataset.iloc[row, col]
        fund = dataset.iloc[row, col + 1]
        fund_stage = str(dataset.iloc[row, col + 2])
        still_in_portfolio = dataset.iloc[row, col + 3]
        participation_round = str(dataset.iloc[row, col + 4]).split(",")
        arr.append([company_id, company_name, firm, fund, fund_stage, still_in_portfolio])
        round_arr.append(participation_round)
        row = row + 1
    rounds = []
    for a, r in zip(arr, round_arr):
        rounds_item = ["", "", "", "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(r)):
            rounds_item[int(r[i]) + 3] = 1
        rounds_item[0] = a[0]
        rounds_item[1] = a[1]
        rounds_item[2] = a[2]
        rounds_item[3] = a[3]
        rounds.append(rounds_item)
    for r in rounds:
        cursor.execute(
            "select participation_history_id from participation_history  where company_id=%s and firm=%s and fund=%s",
            (r[0], r[2], r[3],))
        result2 = cursor.fetchall()
        # 数据库中数据不存在
        if len(result2) == 0:
            cursor.execute(
                "insert into participation_history (company_id,company_name,firm, fund, round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11,round12,round13,round14,round15,round16,round17,round18,round19,round20,round21,round22,round23,round24,round25,round26,round27,round28,round29,round30,round31,round32,round33,round34,round35,round36,round37,round38,round39,round40,round41,round42,round43,round44,round45,round46,round47,round48,round49,round50) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                r)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()

        else:

            query = "update participation_history set round1='%s',round2='%s',round3='%s',round4='%s',round5='%s',round6='%s',round7='%s',round8='%s',round9='%s',round10='%s',round11='%s',round12='%s',round13='%s',round14='%s',round15='%s',round16='%s',round17='%s',round18='%s',round19='%s',round20='%s',round21='%s',round22='%s',round23='%s',round24='%s',round25='%s',round26='%s',round27='%s',round28='%s',round29='%s',round30='%s',round31='%s',round32='%s',round33='%s',round34='%s',round35='%s',round36='%s',round37='%s',round38='%s',round39='%s',round40='%s',round41='%s',round42='%s',round43='%s',round44='%s',round45='%s',round46='%s',round47='%s',round48='%s',round49='%s',round50='%s' where (company_id='%s' and firm='%s' and fund='%s')"
            try:
                cursor.execute(query % (
                    r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17], r[18],
                    r[19], r[20], r[21], r[22], r[23], r[24], r[25], r[26], r[27], r[28],r[29], r[30], r[31], r[32], r[33],
                    r[34], r[35], r[36], r[37], r[38],r[39], r[40], r[41], r[42], r[43],r[44], r[45], r[46], r[47], r[48],
                    r[49], r[50], r[51], r[52], r[53],
                    r[0], pymysql.escape_string(r[2]), pymysql.escape_string(r[3])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
    for a in arr:

        # 插入数据库操作
        cursor.execute(
            "select historical_investors_id from historical_investors where (company_id=%s and firm=%s and fund=%s)",
            (a[0], a[2], a[3],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into historical_investors (company_id,company_name,firm, fund, fund_stage, still_in_portfolio) values(%s,%s,%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
            cursor.execute(
                "select participation_history_id from participation_history  where company_id=%s and firm=%s and fund=%s",
                (r[0], r[2], r[3],))
            result3 = cursor.fetchall()
            participation_round_history_id = result3[0][0]

            query = "update historical_investors set participation_history_id='%s' where (company_id='%s' and firm='%s' and fund='%s')"

            try:
                cursor.execute(
                    query % (
                    participation_round_history_id, a[0], pymysql.escape_string(a[2]), pymysql.escape_string(a[3])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()
        else:

            query = "update historical_investors set fund_stage='%s',still_in_portfolio='%s' where (company_id='%s' and firm='%s' and fund='%s')"

            try:
                cursor.execute(query % (a[4], a[5], a[0], pymysql.escape_string(a[2]), pymysql.escape_string(a[3])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式五，即：更新Products下方的数据
def update_info_complex_products(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    # 关键字的起始位置

    row = location_value.row + 2
    col = location_value.col
    product_name = ""
    while str(dataset.iloc[row, col]) != "nan":
        product_name = dataset.iloc[row, col]
        arr.append([company_id, company_name, product_name])
        row = row + 1
    # 结束查找过程，执行插入数据库操作

    for a in arr:

        # 插入数据库操作
        cursor.execute(
            "select products_id from products where (company_id=%s and product_name=%s)",
            (a[0], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into products (company_id,company_name,product_name) values(%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:

            continue
            # query = "update company_mergers_and_acquisitions set status='%s', deal_value='%s', ev_ebitda='%s', target_financial_advisor='%s', brief_desciption='%s' where (target_name='%s' and acquiror_name='%s' and date='%s')"
            # # print("method_2:", query)
            # try:
            #     cursor.execute(query % (a[5], a[6], [7], pymysql.escape_string(a[8]), pymysql.escape_string(a[9]), pymysql.escape_string(a[3]), a[4], a[2]))
            #     conn.commit()
            # except Exception as e:
            #     print(e)
            #     conn.rollback()


# 更新数据，复杂更新方式六，即：更新Company Officers下方的数据
def update_info_complex_company_officers(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    # 关键字的起始位置

    row = location_value.row + 2
    col = location_value.col
    officer_name = ""
    officer_title = ""

    while str(dataset.iloc[row, col]) != "nan":
        officer_name = dataset.iloc[row, col]
        officer_title = dataset.iloc[row, col + 1]
        arr.append([company_id, company_name, officer_name, officer_title])
        row = row + 1

    for a in arr:

        # 插入数据库操作
        cursor.execute(
            "select officers_id from officers where (company_id=%s and officer_name=%s)",
            (a[0], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into officers (company_id,company_name,officer_name, officer_title) values(%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:

            continue
            query = "update officers set officer_title='%s' where (company_id='%s' and officer_name='%s')"

            try:
                cursor.execute(query % (a[3], pymysql.escape_string(a[0]), pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式七，即：更新Company Directors下方的数据
def update_info_complex_company_directors(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    # 关键字的起始位置

    row = location_value.row + 2
    col = location_value.col
    director_name = ""
    director_title = ""

    while str(dataset.iloc[row, col]) != "nan":
        name = dataset.iloc[row, col]
        title = dataset.iloc[row, col + 1]
        arr.append([company_id, company_name, director_name, director_title])
        row = row + 1

    # 数据库插入操作
    for a in arr:
        # 插入数据库操作
        cursor.execute(
            "select directors_id from directors where (company_id=%s and director_name=%s)",
            (a[0], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into directors (company_id,company_name,director_name, director_title) values(%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:

            continue
            query = "update directors set director_title='%s' where (company_id='%s' and director_name='%s')"

            try:
                cursor.execute(query % (a[3], pymysql.escape_string(a[0]), pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式八，即：更新Income Statement下方的数据
def update_info_complex_key_financials_income(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    arr = []  #
    # 关键字的起始位置
    row = location_value.row
    col = location_value.col + 1
    date = ""
    net_sale_or_revenues = ""
    gross_profit = ""
    total_operating_costs = ""
    total_expenses = ""
    profit_before_tax = ""
    profit_after_tax = ""
    net_income = ""
    count_test = 1

    while str(dataset.iloc[row, col]) != "nan":
        date = dataset.iloc[row, col]
        net_sale_or_revenues = dataset.iloc[row + 1, col]
        gross_profit = dataset.iloc[row + 2, col]
        total_operating_costs = dataset.iloc[row + 3, col]
        total_expenses = dataset.iloc[row + 4, col]
        profit_before_tax = dataset.iloc[row + 5, col]
        profit_after_tax = dataset.iloc[row + 6, col]
        net_income = dataset.iloc[row + 7, col]
        arr.append(
            [company_id, company_name, date, net_sale_or_revenues, gross_profit, total_operating_costs, total_expenses,
             profit_before_tax,
             profit_after_tax, net_income])
        count_test = count_test + 1
        col = col + 1
        if col > (len(dataset.iloc[0, :]) - 1): break
    for a in arr:
        for x in range(len(a)):
            if x>2:
                a[x]="".join(str(a[x]).split(","))
            if a[x] == "-":
                a[x] = ""
    # 数据库插入操作
    for a in arr:
        # 插入数据库操作
        cursor.execute(
            "select income_id from income where (company_id=%s and date=%s)",
            (a[0], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into income (company_id,company_name,date, net_sale_or_revenues, gross_profit, total_operating_costs, total_expenses, profit_before_tax,profit_after_tax, net_income) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:
            query = "update income set net_sale_or_revenues='%s', gross_profit='%s', total_operating_costs='%s', total_expenses='%s', profit_before_tax='%s',profit_after_tax='%s', net_income='%s' where (company_id='%s' and date='%s')"
            try:
                cursor.execute(query % (a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[0], pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式九，即：更新Assets下方的数据
def update_info_complex_key_financials_assets(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name, "-->", location_value.index_key,
    #       "下方的数据插入操作-------------------------------------------------------")
    # 行数
    cols1 = len(dataset.iloc[0, :])
    # 列数
    rows1 = len(dataset.iloc[:, 0])
    # 将原始数据转成矩阵
    data = dataset.as_matrix()
    # 获取行列数据集
    location_list2 = get_col_row(index_key_firm, data, rows1, cols1)
    loc2 = location(0, 0, "Key Financials")

    for loc in location_list2:
        if loc.get_index_key() == "Key Financials":
            loc2.row = loc.row
            loc2.col = loc.col

    row2 = loc2.row + 1
    col2 = loc2.col + 1
    arr = []  #
    # 关键字的起始位置
    row = location_value.row - 1
    col = location_value.col + 1
    date = ""
    cash_and_liquid_assets = ""
    inventory = ""
    current_assets = ""
    tangible_fixed_assets = ""
    non_current_assets = ""
    total_assets = ""
    while str(dataset.iloc[row2, col2]) != "nan":
        date = dataset.iloc[row2, col2]
        cash_and_liquid_assets = dataset.iloc[row + 2, col]
        inventory = dataset.iloc[row + 3, col]
        current_assets = dataset.iloc[row + 4, col]
        tangible_fixed_assets = dataset.iloc[row + 5, col]
        non_current_assets = dataset.iloc[row + 6, col]
        total_assets = dataset.iloc[row + 7, col]
        arr.append(
            [company_id, company_name, date, cash_and_liquid_assets, inventory, current_assets, tangible_fixed_assets,
             non_current_assets,
             total_assets])
        col = col + 1
        col2 = col2 + 1
        if col > (cols1 - 1) or col2 > (cols1):
            # print("已经检索到表的边界，退出循环")
            break;
    for a in arr:
        for x in range(len(a)):
            if x>2:
                a[x]="".join(str(a[x]).split(","))
            if a[x] == "-":
                a[x] = ""

    # 数据库插入操作
    for a in arr:
        # 插入数据库操作
        cursor.execute(
            "select assets_id from assets where (company_id=%s and date=%s)",
            (a[0], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into assets (company_id,company_name,date, cash_and_liquid_assets, inventory, current_assets, tangible_fixed_assets, non_current_assets,total_assets) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                a)
            conn.commit()
        else:
            query = "update assets set cash_and_liquid_assets='%s', inventory='%s', current_assets='%s', tangible_fixed_assets='%s', non_current_assets='%s',total_assets='%s' where (company_id='%s' and date='%s')"
            try:
                cursor.execute(query % (a[3], a[4], a[5], a[6], a[7], a[8], a[0], pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


# 更新数据，复杂更新方式十，即：更新Liabilities下方的数据
def update_info_complex_key_financials_liabilities(dataset, location_value, tablename, company_id, company_name):
    # print("----------开始执行", company_name,"-->",location_value.index_key, "下方的数据插入操作-------------------------------------------------------")
    # 行数
    cols1 = len(dataset.iloc[0, :])
    # 列数
    rows1 = len(dataset.iloc[:, 0])
    # 将原始数据转成矩阵
    data = dataset.as_matrix()
    # 获取行列数据集
    location_list2 = get_col_row(index_key_firm, data, rows1, cols1)
    loc2 = location(0, 0, "")

    for loc in location_list2:
        if loc.get_index_key() == "Key Financials":
            loc2.row = loc.row
            loc2.col = loc.col
    row2 = loc2.row + 1
    col2 = loc2.col + 1
    date = ""
    current_liabilities = ""
    total_debts = ""
    long_term_liabilities = ""
    total_liabilities = ""
    total_shareholders_equity = ""
    total_liabilities_and_shareholders_equity = ""
    arr = []  #
    # 关键字的起始位置
    row = location_value.row + 1
    col = location_value.col + 1
    while str(dataset.iloc[row2, col2]) != "nan":
        date = dataset.iloc[row2, col2]
        current_liabilities = dataset.iloc[row, col]
        total_debts = dataset.iloc[row + 1, col]
        long_term_liabilities = dataset.iloc[row + 2, col]
        total_liabilities = dataset.iloc[row + 3, col]
        total_shareholders_equity = dataset.iloc[row + 5, col]
        total_liabilities_and_shareholders_equity = dataset.iloc[row + 6, col]
        arr.append(
            [company_id, company_name, date, current_liabilities, total_debts, long_term_liabilities, total_liabilities,
             total_shareholders_equity, total_liabilities_and_shareholders_equity])
        col = col + 1
        col2 = col2 + 1
        if col > (cols1 - 1) or col2 > (cols1):
            # print("已经检索到表的边界，退出循环")
            break;
    for a in arr:
        for x in range(len(a)):
            if x>2:
                a[x]="".join(str(a[x]).split(","))
            if a[x] == "-":
                a[x] = ""
    # 数据库插入操作
    for a in arr:
        # 插入数据库操作
        cursor.execute(
            "select liabilities_id from liabilities where (company_id=%s and date=%s)",
            (a[0], a[2],))
        result = cursor.fetchall()
        # 数据库中数据不存在
        if len(result) == 0:
            cursor.execute(
                "insert into liabilities (company_id,company_name,date, current_liabilities, total_debts, long_term_liabilities, total_liabilities,total_shareholders_equity, total_liabilities_and_shareholders_equity) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                a)
            # [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7],a[8],a[9],a[10],a[11],a[12],a[13],a[14]]
            conn.commit()
        else:
            query = "update liabilities set current_liabilities='%s', total_debts='%s', long_term_liabilities='%s', total_liabilities='%s', total_shareholders_equity='%s',total_liabilities_and_shareholders_equity='%s' where (company_id='%s' and date='%s')"
            try:
                cursor.execute(query % (a[3], a[4], a[5], a[6], a[7], a[8], a[0], pymysql.escape_string(a[2])))
                conn.commit()
            except Exception as e:
                print(e)
                conn.rollback()


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


# 联系信息格式化，将联系信息的电话，fax和网址分块并存储
def contact_info_intercept(contact_info):
    arr = ["", "", ""]
    result = str(contact_info).split("|")
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
                if r == "VE Industry Code":  # 如果是这个值说明没有联系方式信息
                    arr[2] = ""
                else:arr[2]=r

        return arr


def obtain_data(path):
    book = xlrd.open_workbook(path)
    # 获取每个sheet的sheetname
    counts = len(book.sheets())

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
            print("检索%s的第%d张sheet" % (path, count + 1))
            conn = myconn.connect( user="root", password="fanxing123456", database="work_company")
            cursor = conn.cursor()
            # 根据表的固定位置的数据插入首次数据
            company_name = book.sheets()[count].row(0)[0].value
            init_arr = init_company_info(origin_data, location_list, company_name)
            excel_id = book.sheets()[count].row(0)[3].value
            found_date = ""
            file_info = path + "--->" + str(count+1)
            print("写入%s的数据到数据库......" % (company_name))
            for loc in location_list:
                if loc.get_index_key() == "Company Founded Date":
                    row = loc.row
                    col = loc.col + 1
                    if str(origin_data.iloc[row][col]) != "nan":
                        found_date = origin_data.iloc[row][col]

            cursor.execute("select company_id,file_info from company_info where name=%s and found_date=%s",
                           (book.sheets()[count].row(0)[0].value, found_date,))

            company_id = 0
            result = cursor.fetchall()
            # 数据库中没有公司信息，插入一条新的记录
            if len(result) == 0:
                excel_id=book.sheets()[count].row(0)[3].value
                init_arr.append(excel_id)
                init_arr.append(file_info)
            #company_name,address_country,address_state,address_city,address_detail,address_code,phone,fax,website,ve_industry_code,sic_code,naic,bussiness_description,found_date,found_year,found_month,found_day,alias,company_status,pe_backed_status,current_operating_stage,total_funding_to_date
                cursor.execute(
                    "insert into company_info (name,address_country,address_state,address_city,address_detail,address_code,phone,fax,website,ve_industry_code,sic_code,naic,bussiness_description,found_date,found_year,found_month,found_day,alias,company_status,pe_backed_status,current_operating_stage,total_funding_to_date,excel_id,file_info) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",init_arr)
                conn.commit()
                # 初次创建数据信息后更新整个表的数据
                cursor.execute("select company_id,file_info from company_info where name=%s and found_date=%s",
                               (company_name, found_date,))
                result = cursor.fetchall()
                company_id = result[0][0]
            else:
                company_id = result[0][0]
                path_before = result[0][1]
                # print("数据库中已有对应的company的信息，跳过")
                if file_info in path_before:
                    print("数据库中已有对应的company的信息，跳过")
                    continue

                else:
                    # print("数据库中已有对应的firm的信息，执行更新")
                    with open('duplicated_company.txt', 'a') as f:
                        f.write(
                            '\n' + "Duplicated info:" + "|Company Name=" + company_name + "| |Path Before Override=" + path_before + "" + "| |Path Now=" + file_info + "|")

                    query = "update company_info set file_info='%s' where company_id='%s'"
                    # print("method_2:", query)
                    try:
                        cursor.execute(query % (pymysql.escape_string((path_before + " + " + file_info)), company_id))
                        conn.commit()
                        return company_id
                    except Exception as e:
                        print(e)
                        conn.rollback()

            # print("----------更新%s的数据-------------------------------------------------------"%(company_name))
            for loc in location_list:

                if loc.get_index_key() == "Last Available Sales Figure":
                    update_info_simple_1_str(origin_data, loc, "company_info", "last_avaliable_sales_figure",
                                             company_id)
                elif loc.get_index_key() == "Legal Counsel":
                    update_info_simple_1_str(origin_data, loc, "company_info", "legal_counsel",
                                             company_id)
                elif loc.get_index_key() == "Post IPO Information":
                    update_info_simple_1_str(origin_data, loc, "company_info", "post_ipo_information",
                                             company_id)
                elif loc.get_index_key() == "   Ticker":
                    update_info_simple_1_str(origin_data, loc, "company_info", "ticker",
                                             company_id)
                elif loc.get_index_key() == "   Exchange":
                    update_info_simple_1_str(origin_data, loc, "company_info", "exchange",
                                             company_id)
                elif loc.get_index_key() == "   IPO Date":
                    update_info_simple_1_str(origin_data, loc, "company_info", "ipo_date",
                                             company_id)
                elif loc.get_index_key() == "Accountant":
                    update_info_simple_1_str(origin_data, loc, "company_info", "accountant",
                                             company_id)
                elif loc.get_index_key() == "   Amount Mil":
                    update_info_simple_1_str(origin_data, loc, "company_info", "amount_mil",
                                             company_id)
                elif loc.get_index_key() == "   Proceeds":
                    update_info_simple_1_str(origin_data, loc, "company_info", "proceeds",
                                             company_id)
                elif loc.get_index_key() == "   Book Manager(s)":
                    update_info_simple_1_str(origin_data, loc, "company_info", "book_managers",
                                             company_id)
                elif loc.get_index_key() == "Business Description":
                    update_info_simple_2_longstr(origin_data, loc, "company_info", "bussiness_description",
                                                 company_id)
                elif loc.get_index_key() == "# of Employees":
                    update_info_simple_1_int(origin_data, loc, "company_info", "num_of_employees",
                                             company_id)
                elif loc.get_index_key() == "Investment Rounds":
                    update_info_complex_inv_rounds(origin_data, loc, "company_investment_rounds", company_id,
                                                   company_name)
                elif loc.get_index_key() == "Mergers and Acquisitions":
                    update_info_complex_merges_and_acquisitions(origin_data, loc,
                                                                "company_mergers_and_acquisitions",
                                                                company_id, company_name)
                elif loc.get_index_key() == "Current Private Equity Investors":
                    update_info_complex_curren_private_equity_investors(origin_data, loc,
                                                                        "company_current_private_equity_investors",
                                                                        company_id, company_name)
                elif loc.get_index_key() == "Historical Private Equity Investors":
                    update_info_complex_historical_private_investors(origin_data, loc,
                                                                     "company_historical_private_investors",
                                                                     company_id, company_name)
                elif loc.get_index_key() == "Company Officers":
                    update_info_complex_company_officers(origin_data, loc, "company_officers", company_id,
                                                         company_name)
                elif loc.get_index_key() == "Company Directors":
                    update_info_complex_company_directors(origin_data, loc, "company_directors", company_id,
                                                          company_name)
                elif loc.get_index_key() == "Products":
                    update_info_complex_products(origin_data, loc, "company_products", company_id, company_name)
                elif loc.get_index_key() == "Income Statement":
                    update_info_complex_key_financials_income(origin_data, loc, "company_key_financials_income",
                                                              company_id, company_name)
                elif loc.get_index_key() == "Assets":
                    update_info_complex_key_financials_assets(origin_data, loc, "company_key_financials_assets",
                                                              company_id, company_name)
                elif loc.get_index_key() == "Liabilities":
                    update_info_complex_key_financials_liabilities(origin_data, loc,
                                                                   "company_key_financials_liabilities", company_id,
                                                                   company_name)
                else:
                    pass

            # print("----------导入%s的数据结束-------------------------------------------------------"%(company_name))


        else:
            print("第%d张sheet中没有数据" % (count + 1))
            continue
    print(path + "所有子表的数据导入结束")
    conn.close()
