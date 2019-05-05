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
    select enterprise_name, region, check_time,to_char(wmsys.wm_concat(distinct mgr_name)) person, check_result from (
        select ver.enterprise_name, dd.code_name region, to_char(d.check_time, 'yyyy-MM-dd') check_time, per.mgr_name, 
        decode(c.check_result, '0', '合格', '1', '不合格', '2', '未在原址经营') check_result from tr_tmg_check_plan p 
        left join tr_tmg_check_plan_detl d on p.oid = d.plan_id
        left join tr_rpt_enterprise_verify ver on d.enterprise_id = ver.enterprise_id
        left join tc_all_dict dd on d.check_dept = dd.code_value and dd.code_type = 'GL0001'
        left join tr_tmg_check_person per on per.pk_id = d.oid
        left join tr_tmg_jg_check c on d.oid = c.plan_detl_id
        where p.year = :year and p.month = :month and c.oid is not null) group by enterprise_name, region, check_time, check_result
    '''
    params = {"year": year, "month": month}
    return dbUtils.get(sql, params)

def export_check_result(result_list, year):
    wb = Workbook()
    for result_dict in result_list:
        print(result_dict)
        for month in result_dict:
            print(month)
            result = result_dict[month]
            print(result)
            sheet = wb.create_sheet(month)

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
    wb.save(str(year) + "年双随机检查纪录.xlsx")


if __name__ == '__main__':
    for year in range(2017, 2020):
        print("year: " + str(year))
        result_list = []
        for i in range(1, 13):
            month = str(i) if i > 9 else '0' + str(i)
            result = get_check_result(year, month)
            result_dict = {month: result}
            result_list.append(result_dict)
        export_check_result(result_list, year)