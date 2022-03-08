#! /usr/bin/env python
#coding:utf-8

from docxtpl import DocxTemplate
import time
import yaml

from star.common.util.OracleDbUtil import OracleDbUtil

resource = yaml.load(open('../conf/bjvm.yaml'), Loader=yaml.FullLoader)
db_host = resource['database']['db_host']
db_name = resource['database']['db_name']
db_username = resource['database']['db_username']
db_password = resource['database']['db_password']

dbUtils = OracleDbUtil(db_host, db_name, db_username, db_password)

# 获取当月维修覆盖的企业数量
def get_current_enterprise_count(start_date_star, end_date_str):
    sql = "select count(distinct r.enterprise_id) from tr_rpt_repair_record r " \
          "where r.out_date >= to_date(:start_date_str, 'yyyyMMdd') and r.out_date < to_date(:end_date_str, 'yyyyMMdd')"
    params = {
        "start_date_str": start_date_str,
        "end_date_str": end_date_str
    }
    res = dbUtils.get_one(sql, params)
    return res[0]


# 获取当月的维修车次数
def get_current_repair_count(start_date_star, end_date_str):
    sql = "select count(oid) from tr_rpt_repair_record r " \
          "where r.out_date >= to_date(:start_date_str, 'yyyyMMdd') and r.out_date < to_date(:end_date_str, 'yyyyMMdd')"
    params = {
        "start_date_str": start_date_str,
        "end_date_str": end_date_str
    }
    res = dbUtils.get_one(sql, params)
    return res[0]


# 获取所有上报维修数据的企业数
def get_total_enterprise_count():
    sql = "select count(distinct enterprise_id) from tr_rpt_repair_record"
    res = dbUtils.get_one(sql)
    return res[0]

# 获取所有上报的维修车次数
def get_total_repair_count():
    sql = "select count(*) from tr_rpt_repair_record"
    res = dbUtils.get_one(sql)
    return res[0]

# 获取指定类型的维修企业数
def get_spec_enterprise_count(spec_repair_type):
    sql = '''
    select count(*) from tr_rpt_enterprise_verify ver 
        left join tc_all_dict d on ver.enterprise_type = d.code_value
        where ver.com_status = '1' and d.code_name like '%'|| :spec_repair_type ||'%'
    '''
    params = {
        "spec_repair_type": spec_repair_type
    }
    print(sql)
    print(params)
    res = dbUtils.get_one(sql, params)
    return res[0]

# 获取上报维修数据的指定类型的维修企业数
def get_spec_upload_enterprise_count(start_date_str, end_date_str, spec_repair_type):
    sql = """select count(distinct r.enterprise_id) from tr_rpt_repair_record r 
            left join tr_rpt_enterprise_verify ver on r.enterprise_id = ver.enterprise_id
            left join tc_all_dict d on ver.enterprise_type = d.code_value 
            where r.out_date >= to_date(:start_date_str, 'yyyyMMdd') and r.out_date < to_date(:end_date_str, 'yyyyMMdd')
            and d.code_name like '%'|| :spec_repair_type ||'%'"""
    params = {
        "start_date_str": start_date_str,
        "end_date_str": end_date_str,
        "spec_repair_type": spec_repair_type
    }
    res = dbUtils.get_one(sql, params)
    return res[0]

if __name__ == '__main__':
    doc = DocxTemplate("健康档案月报表.docx")
    first_class_name = "一类"
    second_class_name = "二类"
    third_class_name = "三类"
    year = "2022"
    month = "02"
    curr_year = time.strftime('%Y', time.localtime(time.time()))
    curr_month = time.strftime('%m', time.localtime(time.time()))
    curr_day = time.strftime('%d', time.localtime(time.time()))
    region_count = 16
    start_date_str = year + (month if int(month) >= 10 else '0' + str(int(month))) + '01'
    if int(month) == 12:
        end_date_str = str(int(year) + 1) + "0101"
    else:
        end_date_str = year + (str(int(month) + 1) if int(month) + 1 >= 10 else '0' + str(int(month) + 1)) + "01"
    print(end_date_str)
    current_enterprise_count = get_current_enterprise_count(start_date_str, end_date_str)
    current_repair_count = get_current_repair_count(start_date_str, end_date_str)
    total_enterprise_count = get_total_enterprise_count()
    total_repair_count = get_total_repair_count()
    first_class_enterprise_count = get_spec_enterprise_count(first_class_name)
    first_class_upload_enterprise_count = get_spec_upload_enterprise_count(start_date_str, end_date_str, first_class_name)
    second_class_enterprise_count = get_spec_enterprise_count(second_class_name)
    second_class_upload_enterprise_count = get_spec_upload_enterprise_count(start_date_str, end_date_str, second_class_name)
    third_class_enterprise_count = get_spec_enterprise_count(third_class_name)
    third_class_upload_enterprise_count = get_spec_upload_enterprise_count(start_date_str, end_date_str, third_class_name)
    fist_class_coverage = round(first_class_upload_enterprise_count / first_class_enterprise_count * 100, 2)
    second_class_coverage = round(second_class_upload_enterprise_count / second_class_enterprise_count * 100, 2)
    third_class_coverage = round(third_class_upload_enterprise_count / third_class_enterprise_count * 100, 2)
    context = {
        "year": year,
        "month": month,
        "curr_year": curr_year,
        "curr_month": curr_month,
        "curr_day": curr_day,
        "region_count": region_count,
        "current_enterprise_count": current_enterprise_count,
        "current_repair_count": current_repair_count,
        "total_enterprise_count": total_enterprise_count,
        "total_repair_count": total_repair_count,
        "first_class_enterprise_count": first_class_upload_enterprise_count,
        "second_class_enterprise_count": second_class_upload_enterprise_count,
        "third_class_enterprise_count": third_class_upload_enterprise_count,
        "first_class_coverage": fist_class_coverage,
        "second_class_coverage": second_class_coverage,
        "third_class_coverage": third_class_coverage
    }
    doc.render(context)
    doc.save(year + "年" + month + "健康档案月报表.docx")