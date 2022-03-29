#! /usr/bin/env python
#coding:utf-8

from docxtpl import DocxTemplate
import time
import yaml

from star.common.util.OracleDbUtil import OracleDbUtil
from star.common.util.MySQLUtil import MySQLUtil

resource = yaml.load(open('../conf/bjvm.yaml'), Loader=yaml.FullLoader)
db_host = resource['database']['db_host']
db_name = resource['database']['db_name']
db_username = resource['database']['db_username']
db_password = resource['database']['db_password']

oracleUtil = OracleDbUtil(db_host, db_name, db_username, db_password)

host = "152.136.97.65"
port = 33307
user = "shopuser"
passwd = "Star@2022A"
db = "lilishop"
mysqlUtil = MySQLUtil(host, port, user, passwd, db)

# 获取当月维修覆盖的企业数量
def get_enterprise_msg():
    sql = """
            select 
               v.ENTERPRISE_NAME                                                                          store_name,
               v.JY_ADDRESS                                                                               store_address_detail,
               a.LONGITUDE || ',' || a.LATITUDE                                                         store_center,
               a.longitude                                                                              store_lon,
               a.LATITUDE                                                                               store_lat,
               v.bus_tel store_phone,
               v.region,
               v.record_num,
               d.code_name enterprise_type,
               v.first_time,
               dd.code_name qal_level
        from TR_RPT_ENTERPRISE_VERIFY v
        left join TR_RPT_ENTERPRISE_ADDRESS a on v.ENTERPRISE_ID = a.ENTERPRISE_ID
        left join tc_all_dict d on v.enterprise_type = d.code_value
        left join tr_rpt_reput_eval_pk p on v.ENTERPRISE_ID = p.ENTERPRISE_ID and p.start_id = '8ca6d6612a7d455da1e41e496a8944fc'
        left join tc_all_dict dd on p.qal_level = dd.code_value and dd.code_type = 'ZLXYDADJ'
        where v.COM_STATUS = 1
        """
    res = oracleUtil.get(sql)
    return res




if __name__ == '__main__':
    enterprise_list = get_enterprise_msg()
    store_logo = "https://aaronwfbucket.oss-cn-beijing.aliyuncs.com/9df3868160d04c198642c12416ba5b08.png"
    create_user = 'stone'
    delete_flag = 0
    store_disable = 'OPEN'
    id = 1500000000000010000

    enterprise_count = len(enterprise_list)
    sql = "insert into li_store(id, create_by, create_time, delete_flag, update_by, update_time, self_operated, " \
          "store_disable, store_logo, store_name, store_address_detail, store_address_path, region_code, " \
          "store_center, store_lon, store_lat, store_desc, store_phone) values "
    store_detail_sql = "insert into li_store_detail(id, company_address, company_name, license_num, store_id) values"
    for index in range(enterprise_count):
        id = id + 1
        item = enterprise_list[index]
        enterprise_name = item[0]
        jy_address = item[1]
        store_center = item[2]
        store_lon = item[3]
        store_lat = item[4]
        store_phone = item[5]
        region_code = item[6]
        record_num = item[7]
        enterprise_type = item[8]
        first_time = item[9]
        qal_level = item[10]
        first_time_str = ''
        area = ''
        try:
            area_index = jy_address.index('区')
            if area_index > -1:
                area = jy_address[3:area_index]
        except Exception as e:
            pass
        if len(str(first_time)) > 10:
            first_time_str = str(first_time)[0:11]
        # print(first_time_str)
        # print("jy_address:" + str(jy_address))
        # print("record_num:" + str(record_num))
        # print("enterprise_type:" + str(enterprise_type))
        # print("first_time_str:" + str(first_time_str))
        # print("store_phone:" + str(store_phone))
        # print("area:" + str(area))
        # print("region_code:" + str(region_code))
        # print("store_center:" + str(store_center))
        # print("store_lon:" + str(store_lon))
        # print("store_lat:" + str(store_lat))
        # print("store_phone:" + str(store_phone))
        # print(id)
        store_phone_str = ''
        if not (store_phone is None):
            store_phone_str = str(store_phone)
        if store_lon is None:
            store_lon = 0
        if store_lat is None:
            store_lat = 0
        if qal_level is None:
            qal_level = ''

        store_desc = '<p>' + enterprise_name + '</p><p>经营地址：' + jy_address + '</p><p>备案编号：' + record_num + \
                     '</p><p>维修类型：' + enterprise_type + '</p><p>开业日期：' + first_time_str + '</p><p>业务电话：' + \
                     store_phone_str + '</p><p>上年度质量信誉考核：' + qal_level + '</p>'

        sql = sql + "(" + str(id) + ", 'stone', now(), 0, 'stone', now(), 0, 'OPEN', 'https://aaronwfbucket.oss-cn-beijing.aliyuncs.com/9df3868160d04c198642c12416ba5b08.png', '" + \
                enterprise_name + "', '" + jy_address + "', concat('北京市,', '" + area + "'), '" + str(region_code) + "', '" + store_center + "', '" + \
                str(store_lon) + "', '" + str(store_lat) + "', '" + store_desc + "', '" + store_phone_str + "'),"
        store_detail_sql = store_detail_sql + "(" + str(id) + ", '" + jy_address + "', '" + enterprise_name + "', '" + record_num + "', " + str(id) + "),"
        if index % 101 == 100 or index == enterprise_count - 1 or index == enterprise_count:
            sql = sql.rstrip(',')
            store_detail_sql = store_detail_sql.rstrip(',')
            count = mysqlUtil.execute(sql)
            print("成功执行，插入数据：" + str(count) + "条。")
            detail_count = mysqlUtil.execute(store_detail_sql)
            print("成功执行，插入数据：" + str(detail_count) + "条。")
            # print(sql)
            sql = "insert into li_store(id, create_by, create_time, delete_flag, update_by, update_time, self_operated, " \
                  "store_disable, store_logo, store_name, store_address_detail, store_address_path, region_code, " \
                  "store_center, store_lon, store_lat, store_desc, store_phone) values "

            store_detail_sql = "insert into li_store_detail(id, company_address, company_name, license_num, store_id) values"

