#! /usr/bin/env python3
# coding: utf-8


import yaml
from openpyxl import Workbook

from star.common.util.OracleDbUtil import OracleDbUtil

resource = yaml.load(open('../conf/bjvm.yaml'))
db_host = resource['database']['db_host']
db_port = resource['database']['db_port']
db_name = resource['database']['db_name']
db_username = resource['database']['db_username']
db_password = resource['database']['db_password']


def get_check_result(year, month):
    resource = yaml.load(open('../conf/bjvm.yaml'))
    db_host = resource['database']['db_host']
    db_name = resource['database']['db_name']
    db_username = resource['database']['db_username']
    db_password = resource['database']['db_password']

    dbUtils = OracleDbUtil(db_host, db_name, db_username, db_password)
    sql = '''
        select v.ENTERPRISE_NAME, v.REGION_NAME, v.CHECK_TIME, to_char(v.CHECK_PERSON), v.CHECK_RESULT_NAME from view_check_list v
            where v.PLAN_FLAG = 1 and v.check_time >= to_date(:year || :month || '01', 'yyyyMMdd') 
            and v.check_time < add_months(to_date(:year || :month || '01', 'yyyyMMdd'), 1)
    '''
    params = {"year": year, "month": month}
    return dbUtils.get(sql, params)

def export_check_result(result, year, month):
    # print(result)
    wb = Workbook()
    # sheetName = year + "年" + month + "双随机检查结果"
    sheet = wb.get_active_sheet()

    sheet['A1'] = "企业名称"
    sheet['B1'] = "区域"
    sheet['C1'] = "检查时间"
    sheet['D1'] = "检查人"
    sheet['E1'] = "检查结果"
    for line, obj in enumerate(result):
        enterprise_name = obj[0]
        region = obj[1]
        check_time = obj[2]
        check_person = obj[3]
        check_result = obj[4]
        sheet['A' + str(line + 2)] = enterprise_name
        sheet['B' + str(line + 2)] = region
        sheet['C' + str(line + 2)] = check_time
        sheet['D' + str(line + 2)] = check_person
        sheet['E' + str(line + 2)] = check_result
    wb.save(str(year) + "年" + str(month) + "月双随机检查纪录.xlsx")


if __name__ == '__main__':
    year = 2019
    month = 10
    result = get_check_result(year, month)
    export_check_result(result, year, month)