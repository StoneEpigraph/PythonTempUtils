#!/usr/loca/env python3
#coding:utf-8

import yaml

from star.common.util.OracleDbUtil import OracleDbUtil

resource = yaml.load(open('../conf/bjvm.yaml'))
db_host = resource['database']['db_host']
db_name = resource['database']['db_name']
db_username = resource['database']['db_username']
db_password = resource['database']['db_password']

dbUtils = OracleDbUtil(db_host, db_name, db_username, db_password)

def get_need_chage_enterprise_chg():
    sql = """
        select * from tr_rpt_enterprise_chg c where c.chg_item = 2 and BEFORE_CONTENT not like '%一%'
        and BEFORE_CONTENT not like '%二%'  and BEFORE_CONTENT not like '%三%'
    """
    return dbUtils.get(sql)

def translation_content(str):
    if not str:
        return ""
    bus_ids = '\'' + str.replace(',', '\',\'') + '\''
    sql = """
        select listagg(enter_type, ';') within group ( order by field_order ) from (
        select dd.code_name || '(' || listagg(d.code_name, ',') within group ( order by d.FIELD_ORDER) || ')' enter_type, dd.FIELD_ORDER from tc_all_dict d
        left join tc_all_dict dd on d.PARENT_CODE_VALUE = dd.code_value
        where d.code_value in (
            %s
            ) group by dd.code_name, dd.FIELD_ORDER)

    """ % bus_ids
    res = dbUtils.get_one(sql)
    if res:
        return res[0]

def update_content_by_id(id, before, after):
    if not id or not before or not after:
        return None
    sql = """
        update tr_rpt_enterprise_chg set before_content = '%s', after_content = '%s' where oid = '%s'
    """ % (before, after, id)
    print(sql)
    return dbUtils.update(sql)

if __name__ == '__main__':
    print('test start')
    # get need change enterpriseChg msg

    res = get_need_chage_enterprise_chg()
    if res and len(res) > 0:
        for item in res:
            oid = item[0]
            enterprise_id = item[1]
            chg_type = item[2]
            chg_item = item[3]
            before_content = item[4]
            after_content = item[10]
            print('before_content: ' + before_content)
            print('after_content: ' + after_content)
            trans_before_content = translation_content(before_content)
            trans_after_content = translation_content(after_content)
            print("trans_before_content: " + trans_before_content)
            print("trans_after_content: " + trans_after_content)

            # update
            update_res = update_content_by_id(oid, trans_before_content, trans_after_content)
            # print("update_res: " + update_res)