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

conn = myconn.connect(user="root", password="Jackey123456", database="work_firm")
cursor = conn.cursor()
cursor.execute(
    "select id,name, fund_status, fund_type, funded, cap_under_mgmt, affiliations,detail_loc, city, state, country, phone, fax, website,file_info from fund_basic_info where  id >=(select id from fund_basic_info order by id ASC LIMIT 0,1)")
result_set_fund_basic_info = cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,company_name, industry, still_in_portfolio, company_status, last_investment_date, location from fund_direct_investments where  id >=(select id from fund_direct_investments order by id ASC LIMIT 0,1)")
result_set_fund_direct_investments= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,name, title, phone, email from fund_executives where  id >=(select id from fund_executives order by id ASC LIMIT 0,1)")
result_set_fund_executives= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,name, size, fund_stage, vintage from fund_funds_managed_by_firm where  id >=(select id from fund_funds_managed_by_firm order by id ASC LIMIT 0,1)")
result_set_fund_funds_managed_by_firm= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, industry_name,num_of_company, sum_inv, avg_per_company, percent_of_inv from fund_investment_profile_industry_breakdown where  id >=(select id from fund_investment_profile_industry_breakdown order by id ASC LIMIT 0,1)")
result_set_fund_investment_profile_industry_breakdown= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, nation_name,num_of_company, sum_inv, avg_per_company, percent_of_inv from fund_investment_profile_nation_breakdown where  id >=(select id from fund_investment_profile_nation_breakdown order by id ASC LIMIT 0,1)")
result_set_fund_investment_profile_nation_breakdown= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, stage_name,num_of_company, sum_inv, avg_per_company, percent_of_inv from fund_investment_profile_stage_breakdown where  id >=(select id from fund_investment_profile_stage_breakdown order by id ASC LIMIT 0,1)")
result_set_fund_investment_profile_stage_breakdown= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, state_name,num_of_company, sum_inv, avg_per_company, percent_of_inv from fund_investment_profile_state_breakdown where  id >=(select id from fund_investment_profile_state_breakdown order by id ASC LIMIT 0,1)")
result_set_fund_investment_profile_state_breakdown= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, status_name,num_of_company, sum_inv, avg_per_company, percent_of_inv from fund_investment_profile_status_breakdown where  id >=(select id from fund_investment_profile_status_breakdown order by id ASC LIMIT 0,1)")
result_set_fund_investment_profile_status_breakdown= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,num_of_company_total, sum_inv_total, avg_per_company_total, percent_of_inv_total, year_name,num_of_company, sum_inv, avg_per_company, percent_of_inv from fund_investment_profile_year_breakdown where  id >=(select id from fund_investment_profile_year_breakdown order by id ASC LIMIT 0,1)")
result_set_fund_investment_profile_year_breakdown= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,detail_loc, city, state, country, phone, fax from fund_other_offices where  id >=(select id from fund_other_offices order by id ASC LIMIT 0,1)")
result_set_fund_other_offices= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,headline, date, publication from fund_related_news where  id >=(select id from fund_related_news order by id ASC LIMIT 0,1)")
result_set_fund_related_news= cursor.fetchall()

cursor.execute(
    "select id,fund_id,fund_name,name, num_of_companies, num_of_rounds from fund_top_co_investors  where  id >=(select id from fund_top_co_investors order by id ASC LIMIT 0,1)")
result_set_fund_top_co_investors= cursor.fetchall()


def get_fund_basic_info_df(result_set):
    id=[]
    name = []
    fund_status = []
    fund_stage = []
    vintage_year = []
    management_firm = []
    fund_size = []
    fund_size_target = []
    fund_investors_type = []
    detail_loc = []
    city = []
    state = []
    country = []
    phone = []
    fax = []
    website = []
    file_info = []
    for result in result_set:
        id.append(result[0])
        name.append(result[1])
        fund_status.append(result[2])
        fund_stage.append(result[3])
        vintage_year.append(result[4])
        management_firm.append(result[5])
        fund_size.append(result[6])
        fund_size_target.append(result[7])
        fund_investors_type.append(result[8])
        detail_loc.append(result[9])
        city.append(result[10])
        state.append(result[11])
        country.append(result[12])
        phone.append(result[13])
        fax.append(result[14])
        website.append(result[15])
        file_info.append(result[16])
    dt={"fund_id":id,"name":name,
        "fund_status":fund_status, "fund_stage":fund_stage,
        "vintage_year":vintage_year, "management_firm":management_firm,
        "fund_size":fund_size,"fund_size_target":fund_size_target,
        "fund_investors_type":fund_investors_type, "detail_loc":detail_loc,
        "city":city, "state":state,
        "country":country, "phone":phone,
        "fax":fax, "website":website,"file_info":file_info}
    cols = ["fund_id","name",
        "fund_status", "fund_stage",
        "vintage_year", "management_firm",
        "fund_size","fund_size_target",
        "fund_investors_type", "detail_loc",
        "city", "state",
        "country", "phone",
        "fax", "website","file_info"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df





def get_fund_direct_investments_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    company_name = []
    industry = []
    still_in_portfolio = []
    company_status = []
    last_investment_date = []
    location = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        company_name.append(result[3])
        industry.append(result[4])
        still_in_portfolio.append(result[5])
        company_status.append(result[6])
        last_investment_date.append(result[7])
        location.append(result[8])
    dt = {"fund_direct_investments_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "company_name":company_name,"industry":industry,
          "still_in_portfolio":still_in_portfolio,"company_status":company_status,
          "last_investment_date":last_investment_date,"location":location}
    cols = ["fund_direct_investments_id","fund_id","fund_name","company_name",
          "industry", "still_in_portfolio",
          "company_status", "last_investment_date",
          "location"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_fund_executives_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    name = []
    title = []
    phone = []
    email = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        name.append(result[3])
        title.append(result[4])
        phone.append(result[5])
        email.append(result[6])
    dt = {"fund_executives_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "name":name, "title":title,
         "phone":phone, "email":email}
    cols = ["fund_executives_id","fund_id","fund_name",
          "name", "title",
         "phone", "email"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df




def get_fund_funds_managed_by_fund_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    name = []
    size = []
    fund_stage = []
    vintage = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        name.append(result[3])
        size.append(result[4])
        fund_stage.append(result[5])
        vintage.append(result[6])
    dt = {"fund_funds_managed_by_fund_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "name":name,"size":size,
          "fund_stage":fund_stage,"vintage":vintage
        }
    cols = ["fund_funds_managed_by_fund_id","fund_id","fund_name",
          "name","size",
          "fund_stage","vintage"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df




def get_fund_investment_profile_industry_breakdown_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    num_of_company_total = []
    sum_inv_total =[]
    avg_per_company_total = []
    percent_of_inv_total =[]
    industry_name = []
    num_of_company = []
    sum_inv = []
    avg_per_company = []
    percent_of_inv = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        num_of_company_total.append(result[3])
        sum_inv_total.append(result[4])
        avg_per_company_total.append(result[5])
        percent_of_inv_total.append(result[6])
        industry_name.append(result[7])
        num_of_company.append(result[8])
        sum_inv.append(result[9])
        avg_per_company.append(result[10])
        percent_of_inv.append(result[11])
    dt = {"fund_investment_profile_industry_breakdown_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "num_of_company_total":num_of_company_total,"sum_inv_total":sum_inv_total,
          "avg_per_company_total":avg_per_company_total,"percent_of_inv_total":percent_of_inv_total,
          "industry_name":industry_name,"num_of_company":num_of_company,
          "sum_inv":sum_inv,"avg_per_company":avg_per_company,
          "percent_of_inv":percent_of_inv
          }
    cols = ["fund_investment_profile_industry_breakdown_id","fund_id","fund_name",
          "num_of_company_total","sum_inv_total",
          "avg_per_company_total","percent_of_inv_total",
          "industry_name","num_of_company",
          "sum_inv","avg_per_company",
          "percent_of_inv"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df

def get_fund_investment_profile_nation_breakdown_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    num_of_company_total = []
    sum_inv_total =[]
    avg_per_company_total = []
    percent_of_inv_total =[]
    nation_name = []
    num_of_company = []
    sum_inv = []
    avg_per_company = []
    percent_of_inv = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        num_of_company_total.append(result[3])
        sum_inv_total.append(result[4])
        avg_per_company_total.append(result[5])
        percent_of_inv_total.append(result[6])
        nation_name.append(result[7])
        num_of_company.append(result[8])
        sum_inv.append(result[9])
        avg_per_company.append(result[10])
        percent_of_inv.append(result[11])
    dt = {"fund_investment_profile_nation_breakdown_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "num_of_company_total":num_of_company_total,"sum_inv_total":sum_inv_total,
          "avg_per_company_total":avg_per_company_total,"percent_of_inv_total":percent_of_inv_total,
          "nation_name":nation_name,"num_of_company":num_of_company,
          "sum_inv":sum_inv,"avg_per_company":avg_per_company,
          "percent_of_inv":percent_of_inv
          }
    cols = ["fund_investment_profile_nation_breakdown_id","fund_id","fund_name",
          "num_of_company_total","sum_inv_total",
          "avg_per_company_total","percent_of_inv_total",
          "nation_name","num_of_company",
          "sum_inv","avg_per_company",
          "percent_of_inv"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_fund_investment_profile_stage_breakdown_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    num_of_company_total = []
    sum_inv_total =[]
    avg_per_company_total = []
    percent_of_inv_total =[]
    stage_name = []
    num_of_company = []
    sum_inv = []
    avg_per_company = []
    percent_of_inv = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        num_of_company_total.append(result[3])
        sum_inv_total.append(result[4])
        avg_per_company_total.append(result[5])
        percent_of_inv_total.append(result[6])
        stage_name.append(result[7])
        num_of_company.append(result[8])
        sum_inv.append(result[9])
        avg_per_company.append(result[10])
        percent_of_inv.append(result[11])
    dt = {"fund_investment_profile_stage_breakdown_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "num_of_company_total":num_of_company_total,"sum_inv_total":sum_inv_total,
          "avg_per_company_total":avg_per_company_total,"percent_of_inv_total":percent_of_inv_total,
          "stage_name":stage_name,"num_of_company":num_of_company,
          "sum_inv":sum_inv,"avg_per_company":avg_per_company,
          "percent_of_inv":percent_of_inv
          }
    cols = ["fund_investment_profile_stage_breakdown_id","fund_id","fund_name",
          "num_of_company_total","sum_inv_total",
          "avg_per_company_total","percent_of_inv_total",
          "stage_name","num_of_company",
          "sum_inv","avg_per_company",
          "percent_of_inv"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_fund_investment_profile_state_breakdown_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    num_of_company_total = []
    sum_inv_total =[]
    avg_per_company_total = []
    percent_of_inv_total =[]
    state_name = []
    num_of_company = []
    sum_inv = []
    avg_per_company = []
    percent_of_inv = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        num_of_company_total.append(result[3])
        sum_inv_total.append(result[4])
        avg_per_company_total.append(result[5])
        percent_of_inv_total.append(result[6])
        state_name.append(result[7])
        num_of_company.append(result[8])
        sum_inv.append(result[9])
        avg_per_company.append(result[10])
        percent_of_inv.append(result[11])
    dt = {"fund_investment_profile_state_breakdown_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "num_of_company_total":num_of_company_total,"sum_inv_total":sum_inv_total,
          "avg_per_company_total":avg_per_company_total,"percent_of_inv_total":percent_of_inv_total,
          "state_name":state_name,"num_of_company":num_of_company,
          "sum_inv":sum_inv,"avg_per_company":avg_per_company,
          "percent_of_inv":percent_of_inv
          }
    cols = ["fund_investment_profile_state_breakdown_id","fund_id","fund_name",
          "num_of_company_total","sum_inv_total",
          "avg_per_company_total","percent_of_inv_total",
          "state_name","num_of_company",
          "sum_inv","avg_per_company",
          "percent_of_inv"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_fund_investment_profile_status_breakdown_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    num_of_company_total = []
    sum_inv_total =[]
    avg_per_company_total = []
    percent_of_inv_total =[]
    status_name = []
    num_of_company = []
    sum_inv = []
    avg_per_company = []
    percent_of_inv = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        num_of_company_total.append(result[3])
        sum_inv_total.append(result[4])
        avg_per_company_total.append(result[5])
        percent_of_inv_total.append(result[6])
        status_name.append(result[7])
        num_of_company.append(result[8])
        sum_inv.append(result[9])
        avg_per_company.append(result[10])
        percent_of_inv.append(result[11])
    dt = {"fund_investment_profile_status_breakdown_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "num_of_company_total":num_of_company_total,"sum_inv_total":sum_inv_total,
          "avg_per_company_total":avg_per_company_total,"percent_of_inv_total":percent_of_inv_total,
          "status_name":status_name,"num_of_company":num_of_company,
          "sum_inv":sum_inv,"avg_per_company":avg_per_company,
          "percent_of_inv":percent_of_inv
          }
    cols = ["fund_investment_profile_status_breakdown_id","fund_id","fund_name",
          "num_of_company_total","sum_inv_total",
          "avg_per_company_total","percent_of_inv_total",
          "status_name","num_of_company",
          "sum_inv","avg_per_company",
          "percent_of_inv"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df

def get_fund_investment_profile_year_breakdown_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    num_of_company_total = []
    sum_inv_total =[]
    avg_per_company_total = []
    percent_of_inv_total =[]
    year_name = []
    num_of_company = []
    sum_inv = []
    avg_per_company = []
    percent_of_inv = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        num_of_company_total.append(result[3])
        sum_inv_total.append(result[4])
        avg_per_company_total.append(result[5])
        percent_of_inv_total.append(result[6])
        year_name.append(result[7])
        num_of_company.append(result[8])
        sum_inv.append(result[9])
        avg_per_company.append(result[10])
        percent_of_inv.append(result[11])
    dt = {"fund_investment_profile_year_breakdown_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "num_of_company_total":num_of_company_total,"sum_inv_total":sum_inv_total,
          "avg_per_company_total":avg_per_company_total,"percent_of_inv_total":percent_of_inv_total,
          "year_name":year_name,"num_of_company":num_of_company,
          "sum_inv":sum_inv,"avg_per_company":avg_per_company,
          "percent_of_inv":percent_of_inv
          }
    cols = ["fund_investment_profile_year_breakdown_id","fund_id","fund_name",
          "num_of_company_total","sum_inv_total",
          "avg_per_company_total","percent_of_inv_total",
          "year_name","num_of_company",
          "sum_inv","avg_per_company",
          "percent_of_inv"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df


def get_fund_other_offices_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    country = []
    state = []
    city = []
    detail_loc = []
    phone = []
    fax = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        country.append(result[3])
        city.append(result[4])
        detail_loc.append(result[5])
        phone.append(result[6])
        fax.append(result[7])
    dt = {"fund_other_offices_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "country":country,"city":city,
          "detail_loc":detail_loc,"phone":phone,
          "fax":fax}
    cols = ["fund_other_offices_id","fund_id","fund_name",
          "country","city",
          "detail_loc","phone",
          "fax"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df



def get_fund_related_news_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    headline = []
    date = []
    publication = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        headline.append(result[3])
        date.append(result[4])
        publication.append(result[5])
    dt = {"fund_related_news_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "headline":headline,"date":date,
          "publication":publication}
    cols = ["fund_related_news_id","fund_id","fund_name",
          "headline","date",
          "publication"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df



def get_fund_top_co_investors_df(result_set):
    id=[]
    fund_id=[]
    fund_name = []
    name = []
    num_of_companies = []
    num_of_rounds = []
    for result in result_set:
        id.append(result[0])
        fund_id.append(result[1])
        fund_name.append(result[2])
        name.append(result[3])
        num_of_companies.append(result[4])
        num_of_rounds.append(result[5])
    dt = {"fund_top_co_investors_id":id,"fund_id":fund_id,"fund_name":fund_name,
          "name":name,"num_of_companies":num_of_companies,
          "num_of_rounds":num_of_rounds}
    cols = ["fund_top_co_investors_id","fund_id","fund_name",
          "name","num_of_companies",
          "num_of_rounds"]
    df = pd.DataFrame(data=dt)
    df = df.ix[:, cols]
    return df

df_fund_basic_info=get_fund_basic_info_df(result_set_fund_basic_info)
df_fund_direct_investments=get_fund_direct_investments_df(result_set_fund_direct_investments)
df_fund_executives=get_fund_executives_df(result_set_fund_executives)
df_fund_funds_managed_by_firm=get_fund_funds_managed_by_fund_df(result_set_fund_funds_managed_by_firm)
df_fund_investment_profile_industry_breakdown=get_fund_investment_profile_industry_breakdown_df(result_set_fund_investment_profile_industry_breakdown)
df_fund_investment_profile_nation_breakdown=get_fund_investment_profile_nation_breakdown_df(result_set_fund_investment_profile_nation_breakdown)
df_fund_investment_profile_stage_breakdown=get_fund_investment_profile_stage_breakdown_df(result_set_fund_investment_profile_stage_breakdown)
df_fund_investment_profile_state_breakdown=get_fund_investment_profile_state_breakdown_df(result_set_fund_investment_profile_state_breakdown)
df_fund_investment_profile_status_breakdown=get_fund_investment_profile_status_breakdown_df(result_set_fund_investment_profile_status_breakdown)
df_fund_investment_profile_year_breakdown=get_fund_investment_profile_year_breakdown_df(result_set_fund_investment_profile_year_breakdown)
df_fund_other_offices=get_fund_other_offices_df(result_set_fund_other_offices)
df_fund_related_news=get_fund_related_news_df(result_set_fund_related_news)
df_fund_top_co_investors=get_fund_top_co_investors_df(result_set_fund_top_co_investors)


if os.path.exists("firm.xls"):
    pass


else:
    df_final_fund_basic_info=df_fund_basic_info
    df_final_fund_direct_investments=df_fund_direct_investments
    df_final_fund_executives=df_fund_executives
    df_final_fund_funds_managed_by_firm=df_fund_funds_managed_by_firm
    df_final_fund_investment_profile_industry_breakdown=df_fund_investment_profile_industry_breakdown
    df_final_fund_investment_profile_nation_breakdown=df_fund_investment_profile_nation_breakdown
    df_final_fund_investment_profile_stage_breakdown=df_fund_investment_profile_stage_breakdown
    df_final_fund_investment_profile_state_breakdown=df_fund_investment_profile_state_breakdown
    df_final_fund_investment_profile_status_breakdown=df_fund_investment_profile_status_breakdown
    df_final_fund_investment_profile_year_breakdown=df_fund_investment_profile_year_breakdown
    df_final_fund_other_offices=df_fund_other_offices
    df_final_fund_related_news=df_fund_related_news
    df_final_fund_top_co_investors=df_fund_top_co_investors

writer = pd.ExcelWriter("firm.xls")
df_final_fund_basic_info.to_excel(writer, "firm info", index=False)
df_final_fund_direct_investments.to_excel(writer, "direct investments", index=False)
df_final_fund_executives.to_excel(writer, "executives", index=False)
df_final_fund_funds_managed_by_firm.to_excel(writer, "funds managed", index=False)
df_final_fund_investment_profile_industry_breakdown.to_excel(writer, "industry breakdown", index=False)
df_final_fund_investment_profile_nation_breakdown.to_excel(writer, "nation breakdown", index=False)
df_final_fund_investment_profile_stage_breakdown.to_excel(writer, "stage breakdown", index=False)
df_final_fund_investment_profile_state_breakdown.to_excel(writer, "state breakdown", index=False)
df_final_fund_investment_profile_status_breakdown.to_excel(writer, "status breakdown", index=False)
df_final_fund_investment_profile_year_breakdown.to_excel(writer, "year breakdown", index=False)
df_final_fund_other_offices.to_excel(writer, "other offices", index=False)
df_final_fund_related_news.to_excel(writer, "related news", index=False)
df_final_fund_top_co_investors.to_excel(writer, "top co_investors", index=False)

writer.save()
