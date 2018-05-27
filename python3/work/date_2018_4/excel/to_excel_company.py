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

conn = myconn.connect(user="root", password="Jackey123456", database="work_company")
cursor = conn.cursor()
cursor.execute(
    "select id,name,address,sic_code,naic,company_status,company_founded_date,contact_info_phone,contact_info_fax,contact_info_website,ve_industry_code,bussiness_description,pe_backed_status,total_funding_to_date,alias,operating_stage,num_of_employees,last_avaliable_sales_figure,current_operating_status,legal_counsel,post_ipo_information,ticker,exchange,ipo_date,accountant,amount_mil,proceeds,book_managers,file_info from company_info where  id >(select id from company_info order by id ASC LIMIT 0,1)")
result_set_company_info = cursor.fetchall()
description=cursor.description
print(description)

cursor.execute(
    "select id,company_id,company_name,firm,fund,fund_stage,participation_round_id from company_current_private_equity_investors where  id >(select id from company_current_private_equity_investors order by id ASC LIMIT 0,1)")
result_set_company_current_private_equity_investors = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,director_name,director_title from company_directors where  id >(select id from company_directors order by id ASC LIMIT 0,1)")
result_set_company_directors = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,firm, fund, round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11,round12,round13,round14,round15,round16,round17,round18,round19,round20,round21,round22,round23,round24,round25 from participation_round where  id >(select id from participation_round order by id ASC LIMIT 0,1)")
result_set_participation_round = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,firm, fund, round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11,round12,round13,round14,round15,round16,round17,round18,round19,round20,round21,round22,round23,round24,round25 from participation_round_history where  id >(select id from participation_round_history order by id ASC LIMIT 0,1)")
result_set_participation_round_history = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,firm,fund,fund_stage,still_in_portfolio,participation_round_history_id from company_historical_private_investors where  id >(select id from company_historical_private_investors order by id ASC LIMIT 0,1)")
result_set_company_historical_private_investors = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,date,num_of_inv,stage,deal_value,equity_amount,pe_debt_amt,company_valuation,investment_location,firm,fund,fund_security_type,p_equity_amount,debt from company_investment_rounds where  id >(select id from company_investment_rounds order by id ASC LIMIT 0,1)")
result_set_company_investment_rounds = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,date,cash_and_liquid_assets,inventory,current_assets,tangible_fixed_assets,non_current_assets,total_assets from company_key_financials_assets where  id >(select id from company_key_financials_assets order by id ASC LIMIT 0,1)")
result_set_company_key_financials_assets = cursor.fetchall()


cursor.execute(
    "select id,company_id,company_name,date, net_sale_or_revenues, gross_profit, total_operating_costs, total_expenses, profit_before_tax,profit_after_tax, net_income from company_key_financials_income where  id >(select id from company_key_financials_income order by id ASC LIMIT 0,1)")
result_set_company_key_financials_income = cursor.fetchall()

cursor.execute(
    "select id,company_id, company_name, date, current_liabilities, total_debts, long_term_liabilities, total_liabilities,total_shareholders_equity, total_liabilities_and_shareholders_equity from company_key_financials_liabilities where  id >(select id from company_key_financials_liabilities order by id ASC LIMIT 0,1)")
result_set_company_key_financials_liabilities = cursor.fetchall()


cursor.execute(
    "select id,company_id,company_name,date, target_name, acquiror_name, status, deal_value, ev_ebitda, target_financial_advisor,brief_desciption from company_mergers_and_acquisitions where  id >(select id from company_mergers_and_acquisitions order by id ASC LIMIT 0,1)")
result_set_company_mergers_and_acquisitions = cursor.fetchall()

cursor.execute(
    "select id,company_id,company_name,officer_name, officer_title from company_officers where  id >(select id from company_officers order by id ASC LIMIT 0,1)")
result_set_company_officers = cursor.fetchall()


cursor.execute(
    "select id,company_id,company_name,product_name from company_products where  id >(select id from company_products order by id ASC LIMIT 0,1)")
result_set_company_products = cursor.fetchall()



def get_company_info_df(result_set_company_info):
    print(len(result_set_company_info))
    # print(result_set)
    # print(result_set[1][0])
    company_id = []
    address = []
    name = []
    sic_code = []
    naic = []
    company_status = []
    company_founded_date = []
    phone = []
    fax = []
    website = []
    ve_industry_code = []
    bussiness_description = []
    pe_backed_status = []
    total_funding_to_date = []
    alias = []
    operating_stage = []
    num_of_employees = []
    last_avaliable_sales_figure = []
    current_operating_status = []
    legal_counsel = []
    post_ipo_information = []
    ticker = []
    exchange = []
    ipo_date = []
    accountant = []
    amount_mil = []
    proceeds = []
    book_managers = []
    file_info = []
    for result in result_set_company_info:
        company_id.append(result[0])
        name.append(result[1])
        address.append(result[2])
        sic_code.append(result[3])
        naic.append(result[4])
        company_status.append(result[5])
        company_founded_date.append(result[6])
        phone.append(result[7])
        fax.append(result[8]),
        website.append(result[9]),
        ve_industry_code.append(result[10]),
        bussiness_description.append(result[11]),
        pe_backed_status.append(result[12]),
        total_funding_to_date.append(result[13]),
        alias.append(result[14]),
        operating_stage.append(result[15]),
        num_of_employees.append(result[16]),
        last_avaliable_sales_figure.append(result[17]),
        current_operating_status.append(result[18]),
        legal_counsel.append(result[19]),
        post_ipo_information.append(result[20]),
        ticker.append(result[21]),
        exchange.append(result[22]),
        ipo_date.append(result[23]),
        accountant.append(result[24]),
        amount_mil.append(result[25]),
        proceeds.append(result[26]),
        book_managers.append(result[27]),
        file_info.append(result[28])

    dt_company_info = {"Company ID": company_id, "Name": name, "Address": address, "SIC Code": sic_code, "NAIC": naic,
                       "Status": company_status, "Funded Date": company_founded_date,
                       "Phone": phone, "Fax": fax, "Website": website, "VE Industry Code": ve_industry_code,
                       "Description": bussiness_description, "PE Backed Status": pe_backed_status,
                       "Total Funding To Date": total_funding_to_date, "Alias": alias,
                       "Operating Stage": operating_stage,
                       "Num of Employees": num_of_employees, "Last Avaliable Sales Figure": last_avaliable_sales_figure,
                       "Current Operating Status": current_operating_status, "Legal Counsel": legal_counsel,
                       "Post IPO Information": post_ipo_information, "Ticker": ticker, "Exchange": exchange,
                       "IPO Date": ipo_date, "Accountant": accountant, "Amount Mil": amount_mil, "Proceeds": proceeds,
                       "Book Managers": book_managers, "File Info": file_info}
    df_company_info = pd.DataFrame(data=dt_company_info)
    cols = ["Company ID", "Name", "Address", "SIC Code", "NAIC", "Status", "Funded Date", "Phone", "Fax", "Website",
            "VE Industry Code", "Description", "PE Backed Status", "Total Funding To Date", "Alias", "Operating Stage",
            "Num of Employees", "Last Avaliable Sales Figure", "Current Operating Status", "Legal Counsel",
            "Post IPO Information", "Ticker", "Exchange", "IPO Date", "Accountant", "Amount Mil", "Proceeds",
            "Book Managers", "File Info"]
    df_company_info = df_company_info.ix[:, cols]
    return df_company_info


def get_company_current_private_equity_investors_df(result_set_company_current_private_equity_investors):
    id = []
    company_id = []
    company_name = []
    firm = []
    fund = []
    fund_stage = []
    participation_round_id = []
    for result in result_set_company_current_private_equity_investors:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        firm.append(result[3])
        fund.append(result[4])
        fund_stage.append(result[5])
        participation_round_id.append(result[6])
    dt_company_current_private_equity_investors = {"Company Current Private Equity Investors ID": id,
                                                   "Company ID": company_id, "Company Name": company_name, "Firm": firm,
                                                   "Fund": fund, "Fund Stage": fund_stage,
                                                   "Participation Round ID": participation_round_id}
    cols = ["Company Current Private Equity Investors ID", "Company ID", "Company Name", "Firm", "Fund", "Fund Stage",
            "Participation Round ID"]
    df_company_current_private_equity_investors = pd.DataFrame(data=dt_company_current_private_equity_investors)
    df_company_current_private_equity_investors = df_company_current_private_equity_investors.ix[:, cols]
    return df_company_current_private_equity_investors


def get_company_directors_df(result_set_company_directors):
    id = []
    company_id = []
    company_name = []
    director_name = []
    director_title = []
    for result in result_set_company_directors:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        director_name.append(result[3])
        director_title.append(result[4])
    dt_company_directors = {"Company Directors ID": id, "Company ID": company_id, "Company Name": company_name,
                            "Director Name": director_name, "Director Title": director_title}
    cols = ["Company Directors ID", "Company ID", "Company Name", "Director Name", "Director Title"]
    df_company_directors = pd.DataFrame(data=dt_company_directors)
    df_company_directors = df_company_directors.ix[:, cols]
    return df_company_directors


def get_participation_round(result_set):
    id = []
    company_id = []
    company_name = []
    firm = []
    fund = []
    round1 = []
    round2 = []
    round3 = []
    round4 = []
    round5 = []
    round6 = []
    round7 = []
    round8 = []
    round9 = []
    round10 = []
    round11 = []
    round12 = []
    round13 = []
    round14 = []
    round15 = []
    round16 = []
    round17 = []
    round18 = []
    round19 = []
    round20 = []
    round21 = []
    round22 = []
    round23 = []
    round24 = []
    round25 = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        firm.append(result[3])
        fund.append(result[4])
        round1.append(result[5])
        round2.append(result[6])
        round3.append(result[7])
        round4.append(result[8])
        round5.append(result[9])
        round6.append(result[10])
        round7.append(result[11])
        round8.append(result[12])
        round9.append(result[13])
        round10.append(result[14])
        round11.append(result[15])
        round12.append(result[16])
        round13.append(result[17])
        round14.append(result[18])
        round15.append(result[19])
        round16.append(result[20])
        round17.append(result[21])
        round18.append(result[22])
        round19.append(result[23])
        round20.append(result[24])
        round21.append(result[25])
        round22.append(result[26])
        round23.append(result[27])
        round24.append(result[28])
        round25.append(result[29])

    dt = {"Participation Round ID": id,
          "Company ID": company_id, "Company Name": company_name, "Firm": firm,
          "Fund": fund, "round1": round1, "round2": round2, "round3": round3,
          "round4": round4, "round5": round5, "round6": round6,
          "round7": round7, "round8": round8, "round9": round9,
          "round10": round10, "round11": round11, "round12": round12,
          "round13": round13, "round14": round14, "round15": round15,
          "round16": round16, "round17": round17, "round18": round18,
          "round19": round19, "round20": round20, "round21": round21,
          "round22": round22, "round23": round23, "round24": round24,
          "round25": round25
          }
    cols = ["Participation Round ID", "Company ID", "Company Name", "Firm", "Fund", "round1",
            "round2", "round3", "round4", "round5", "round6", "round7", "round8", "round9", "round10", "round11",
            "round12", "round13", "round14", "round15", "round16", "round17", "round18", "round19", "round20",
            "round21", "round22", "round23", "round24", "round25"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_participation_round_history(result_set):
    id = []
    company_id = []
    company_name = []
    firm = []
    fund = []
    round1 = []
    round2 = []
    round3 = []
    round4 = []
    round5 = []
    round6 = []
    round7 = []
    round8 = []
    round9 = []
    round10 = []
    round11 = []
    round12 = []
    round13 = []
    round14 = []
    round15 = []
    round16 = []
    round17 = []
    round18 = []
    round19 = []
    round20 = []
    round21 = []
    round22 = []
    round23 = []
    round24 = []
    round25 = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        firm.append(result[3])
        fund.append(result[4])
        round1.append(result[5])
        round2.append(result[6])
        round3.append(result[7])
        round4.append(result[8])
        round5.append(result[9])
        round6.append(result[10])
        round7.append(result[11])
        round8.append(result[12])
        round9.append(result[13])
        round10.append(result[14])
        round11.append(result[15])
        round12.append(result[16])
        round13.append(result[17])
        round14.append(result[18])
        round15.append(result[19])
        round16.append(result[20])
        round17.append(result[21])
        round18.append(result[22])
        round19.append(result[23])
        round20.append(result[24])
        round21.append(result[25])
        round22.append(result[26])
        round23.append(result[27])
        round24.append(result[28])
        round25.append(result[29])

    dt = {"Participation Round History ID": id,
          "Company ID": company_id, "Company Name": company_name, "Firm": firm,
          "Fund": fund, "round1": round1, "round2": round2, "round3": round3,
          "round4": round4, "round5": round5, "round6": round6,
          "round7": round7, "round8": round8, "round9": round9,
          "round10": round10, "round11": round11, "round12": round12,
          "round13": round13, "round14": round14, "round15": round15,
          "round16": round16, "round17": round17, "round18": round18,
          "round19": round19, "round20": round20, "round21": round21,
          "round22": round22, "round23": round23, "round24": round24,
          "round25": round25
          }
    cols = ["Participation Round History ID", "Company ID", "Company Name", "Firm", "Fund", "round1",
            "round2", "round3", "round4", "round5", "round6", "round7", "round8", "round9", "round10", "round11",
            "round12", "round13", "round14", "round15", "round16", "round17", "round18", "round19", "round20",
            "round21", "round22", "round23", "round24", "round25"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_company_historical_private_investors_df(result_set):
    id = []
    company_id = []
    company_name = []
    firm = []
    fund = []
    fund_stage = []
    still_in_portfolio = []
    participation_round_history_id = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        firm.append(result[3])
        fund.append(result[4])
        fund_stage.append(result[5])
        still_in_portfolio.append(result[6])
        participation_round_history_id.append(result[7])

    dt = {"Company Historical Private Investors ID": id, "Company ID": company_id, "Company Name": company_name,
          "Firm": firm, "Fund": fund, "Fund Stage": fund_stage, "Still in Portfolio": still_in_portfolio,
          "Participation Round History ID": participation_round_history_id}
    cols = ["Company Historical Private Investors ID", "Company ID", "Company Name", "Firm", "Fund", "Fund Stage",
            "Still in Portfolio", "Participation Round History ID"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_company_investment_rounds_df(result_set):
    id = []
    company_id = []
    company_name = []
    date = []
    num_of_inv = []
    stage = []
    deal_value = []
    equity_amount = []
    pe_debt_amt = []
    company_valuation = []
    investment_location = []
    firm = []
    fund = []
    fund_security_type = []
    p_equity_amount = []
    debt = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        date.append(result[3])
        num_of_inv.append(result[4])
        stage.append(result[5])
        deal_value.append(result[6])
        equity_amount.append(result[7])
        pe_debt_amt.append(result[8])
        company_valuation.append(result[9])
        investment_location.append(result[10])
        firm.append(result[11])
        fund.append(result[12])
        fund_security_type.append(result[13])
        p_equity_amount.append(result[14])
        debt.append(result[15])
    dt = {"Company Investment Rounds ID": id, "Company ID": company_id, "Company Name": company_name, "Date": date,
          "Num of inv": num_of_inv, "Stage": stage, "Deal Value": deal_value, "Equity Amount": equity_amount,
          "PE Debt Amt": pe_debt_amt, "Company Valuation": company_valuation,
          "Investment Location": investment_location, "Firm": firm, "Fund": fund,
          "Fund Security Type": fund_security_type, "Personal Equity Amount": p_equity_amount, "Debt": debt}
    cols = ["Company Investment Rounds ID", "Company ID", "Company Name", "Date", "Num of inv", "Stage", "Deal Value",
            "Equity Amount", "PE Debt Amt", "Company Valuation", "Investment Location", "Firm", "Fund",
            "Fund Security Type", "Personal Equity Amount", "Debt"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df
def get_company_key_financials_assets_df(result_set):
    id = []
    company_id = []
    company_name = []
    date = []
    cash_and_liquid_assets=[]
    inventory=[]
    current_assets=[]
    tangible_fixed_assets=[]
    non_current_assets=[]
    total_assets=[]
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        date.append(result[3])
        cash_and_liquid_assets.append(result[4])
        inventory.append(result[5])
        current_assets.append(result[6])
        tangible_fixed_assets.append(result[7])
        non_current_assets.append(result[8])
        total_assets.append(result[9])

    dt = {"Company Key Financials Assets ID": id, "Company ID": company_id, "Company Name": company_name, "Date": date,
          "Cash and Liquid Assets": cash_and_liquid_assets, "Inventory": inventory, "Current Assets": current_assets, "Tangible Fixed Assets": tangible_fixed_assets,
          "Non Current Assets": non_current_assets, "Total Assets": total_assets}
    cols = ["Company Key Financials Assets ID", "Company ID", "Company Name", "Date",
          "Cash and Liquid Assets", "Inventory", "Current Assets", "Tangible Fixed Assets",
          "Non Current Assets", "Total Assets"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df

def get_company_key_financials_income_df(result_set):
    id = []
    company_id = []
    company_name = []
    date = []
    net_sale_or_revenues = []
    gross_profit = []
    total_operating_costs = []
    total_expenses = []
    profit_before_tax = []
    profit_after_tax = []
    net_income = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        date.append(result[3])
        net_sale_or_revenues.append(result[4])
        gross_profit.append(result[5])
        total_operating_costs.append(result[6])
        total_expenses.append(result[7])
        profit_before_tax.append(result[8])
        profit_after_tax.append(result[9])
        net_income.append(result[10])

    dt = {"Company Key Financials Income ID": id, "Company ID": company_id, "Company Name": company_name, "Date": date,
          "Net Sale or Revenues": net_sale_or_revenues, "Gross Profit": gross_profit, "Total Operating Costs": total_operating_costs, "Total Expenses": total_expenses,
          "Profit Before Tax": profit_before_tax, "Profit After Tax": profit_after_tax,"Net Income":net_income}
    cols = ["Company Key Financials Income ID", "Company ID", "Company Name", "Date",
          "Net Sale or Revenues", "Gross Profit", "Total Operating Costs", "Total Expenses",
          "Profit Before Tax", "Profit After Tax","Net Income"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df

def get_company_key_financials_liabilities_df(result_set):
    id = []
    company_id = []
    company_name = []
    date = []
    current_liabilities = []
    total_debts = []
    long_term_liabilities = []
    total_liabilities = []
    total_shareholders_equity = []
    total_liabilities_and_shareholders_equity = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        date.append(result[3])
        current_liabilities.append(result[4])
        total_debts.append(result[5])
        long_term_liabilities.append(result[6])
        total_liabilities.append(result[7])
        total_shareholders_equity.append(result[8])
        total_liabilities_and_shareholders_equity.append(result[9])

    dt = {"Company Key Financials Liabilities ID": id, "Company ID": company_id, "Company Name": company_name, "Date": date,
          "Current Liabilities":current_liabilities,"Total Debts":total_debts,"Long Term Liabilities":long_term_liabilities,
          "Total Liabilities":total_liabilities,"Total Shareholders Equity":total_shareholders_equity,"Total Liabilities and Shareholders Equity":total_liabilities_and_shareholders_equity
          }
    cols = ["Company Key Financials Liabilities ID", "Company ID", "Company Name", "Date",
          "Current Liabilities","Total Debts","Long Term Liabilities",
          "Total Liabilities","Total Shareholders Equity","Total Liabilities and Shareholders Equity"
          ]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df
def get_company_mergers_and_acquisitions_df(result_set):
    id = []
    company_id = []
    company_name = []
    date = []
    target_name = []
    acquiror_name = []
    status = []
    deal_value = []
    ev_ebitda = []
    target_financial_advisor = []
    brief_desciption = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        date.append(result[3])
        target_name.append(result[4])
        acquiror_name.append(result[5])
        status.append(result[6])
        deal_value.append(result[7])
        ev_ebitda.append(result[8])
        target_financial_advisor.append(result[9])
        brief_desciption.append(result[10])

    dt = {"Company Mergers and Acquisitions ID": id, "Company ID": company_id, "Company Name": company_name, "Date": date,
          "Target Name":target_name,"Acquiror Name":acquiror_name,
          "Status":status,"Deal Value":deal_value,"EV Ebitda":ev_ebitda,
          "Target Financial Advisor":target_financial_advisor,"Brief Desciption":brief_desciption

          }
    cols = ["Company Mergers and Acquisitions ID", "Company ID", "Company Name", "Date",
            "Target Name", "Acquiror Name",
    "Status", "Deal Value", "EV Ebitda",
    "Target Financial Advisor", "Brief Desciption"
          ]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df

def get_company_officers_df(result_set):
    id = []
    company_id = []
    company_name = []
    officer_name = []
    officer_title = []
    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        officer_name.append(result[3])
        officer_title.append(result[4])

    dt = {"Company Officers ID": id, "Company ID": company_id, "Company Name": company_name,
          "Officer Name":officer_name,"Officer Title":officer_title
          }
    cols = ["Company Officers ID", "Company ID", "Company Name",
          "Officer Name","Officer Title"
          ]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_company_products_df(result_set):
    id = []
    company_id = []
    company_name = []
    product_name = []

    for result in result_set:
        id.append(result[0])
        company_id.append(result[1])
        company_name.append(result[2])
        product_name.append(result[3])

    dt = {"Company Products ID": id, "Company ID": company_id, "Company Name": company_name,"Product Name":product_name
          }
    cols = ["Company Products ID", "Company ID", "Company Name","Product Name"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


df_company_info = get_company_info_df(result_set_company_info)
df_company_current_private_equity_investors = get_company_current_private_equity_investors_df(
    result_set_company_current_private_equity_investors)
df_company_directors = get_company_directors_df(result_set_company_directors)

df_participation_round = get_participation_round(result_set_participation_round)
df_company_historical_private_investors = get_company_historical_private_investors_df(
    result_set_company_historical_private_investors)
df_participation_round_histroy = get_participation_round(result_set_participation_round_history)
df_company_investment_rounds=get_company_investment_rounds_df(result_set_company_investment_rounds)
df_company_key_financials_assets=get_company_key_financials_assets_df(result_set_company_key_financials_assets)
df_company_key_financials_income=get_company_key_financials_income_df(result_set_company_key_financials_income)
df_company_key_financials_liabilities=get_company_key_financials_liabilities_df(result_set_company_key_financials_liabilities)
df_company_mergers_and_acquisitions=get_company_mergers_and_acquisitions_df(result_set_company_mergers_and_acquisitions)
df_company_officers=get_company_officers_df(result_set_company_officers)
df_company_products=get_company_products_df(result_set_company_products)

if os.path.exists("company.xls"):
    pass
    # df_origin_company_info = pd.DataFrame(pd.read_excel("company.xls", sheet_name="company info"))
    # df_final_company_info = pd.merge(df_company_info, df_origin_company_info, on="Company ID", how="outer")
    #
    # df_origin_company_current_private_equity_investors = pd.DataFrame(
    #     pd.read_excel("company.xls", sheet_name="current equity investors"))
    # df_final_company_current_private_equity_investors = pd.merge(df_company_current_private_equity_investors,
    #                                                              df_origin_company_current_private_equity_investors,
    #                                                              on="Company Current Private Equity Investors ID",
    #                                                              how="outer")
    #
    # df_origin_company_directors = pd.DataFrame(pd.read_excel("company.xls", sheet_name="company directors"))
    # df_final_company_directors = pd.merge(df_company_directors, df_origin_company_directors, on="Company Directors ID",
    #                                       how="outer")
    #
    # df_origin_participation_round = pd.DataFrame(pd.read_excel("company.xls", sheet_name="participation rounds"))
    # df_final_participation_round = pd.merge(df_participation_round, df_origin_participation_round,
    #                                         on="Participation Round ID",
    #                                         how="outer")
    #
    # df_origin_company_historical_private_investors = pd.DataFrame(
    #     pd.read_excel("company.xls", sheet_name="history investors"))
    # df_final_company_historical_private_investors = pd.merge(df_company_historical_private_investors,
    #                                                          df_origin_company_historical_private_investors,
    #                                                          on="Company Historical Private Investors ID",
    #                                                          how="outer")
    #
    # df_origin_participation_round_histroy = pd.DataFrame(
    #     pd.read_excel("company.xls", sheet_name="history participation"))
    # df_final_participation_round_history = pd.merge(df_participation_round_histroy,
    #                                                 df_origin_participation_round_histroy, on="Participation Round ID",
    #                                                 how="outer")
    #
    # df_origin_company_investment_rounds = pd.DataFrame(
    #     pd.read_excel("company.xls", sheet_name="investment rounds"))
    # df_final_company_investment_rounds = pd.merge(df_company_investment_rounds,
    #                                                 df_origin_company_investment_rounds, on="Company Investment Rounds ID",
    #                                                 how="outer")


else:
    df_final_company_info = df_company_info
    df_final_company_current_private_equity_investors = df_company_current_private_equity_investors
    df_final_company_directors = df_company_directors
    df_final_participation_round = df_participation_round
    df_final_company_historical_private_investors = df_company_historical_private_investors
    df_final_participation_round_history = df_participation_round_histroy
    df_final_company_investment_rounds = df_company_investment_rounds
    df_final_company_key_financials_assets=df_company_key_financials_assets
    df_final_company_key_financials_income=df_company_key_financials_income
    df_final_company_key_financials_liabilities=df_company_key_financials_liabilities
    df_final_company_mergers_and_acquisitions=df_company_mergers_and_acquisitions
    df_final_company_officers=df_company_officers
    df_final_company_products=df_company_products

writer = pd.ExcelWriter("company.xls")
df_final_company_info.to_excel(writer, "company info", index=False)
df_final_company_current_private_equity_investors.to_excel(writer, "current equity investors", index=False)
df_final_company_directors.to_excel(writer, "company directors", index=False)
df_final_participation_round.to_excel(writer, "participation rounds", index=False)
df_final_company_historical_private_investors.to_excel(writer, "history investors", index=False)
df_final_participation_round_history.to_excel(writer, "history participation", index=False)
df_final_company_investment_rounds.to_excel(writer, "investment rounds", index=False)
df_final_company_key_financials_assets.to_excel(writer, "assets", index=False)
df_final_company_key_financials_income.to_excel(writer, "income", index=False)
df_final_company_key_financials_liabilities.to_excel(writer, "liabilities", index=False)
df_final_company_mergers_and_acquisitions.to_excel(writer, "mergers acquisitions", index=False)
df_final_company_officers.to_excel(writer, "officers", index=False)
df_final_company_products.to_excel(writer, "products", index=False)

writer.save()
