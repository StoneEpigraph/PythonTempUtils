#!/usr/bin/env python3
# coding: utf-8

import yaml
import pandas as pd
from pandas import DataFrame

from star.common.util.OracleDbPoolUtil import OracleDbUtil

resource = yaml.load(open('conf/bjvm.yaml'), Loader=yaml.FullLoader)
db_host = resource['database']['db_host']
db_name = resource['database']['db_name']
db_username = resource['database']['db_username']
db_password = resource['database']['db_password']

dbUtils = OracleDbUtil(db_host, db_name, db_username, db_password)

def hasEnvCheckRecord(vehicle_num):
    sql = "select count(*) nums from hb_vehicle_check_data d where d.vehicle_num = :vehicle_num";
    params = {
        'vehicle_num': vehicle_num
    }
    res = dbUtils.get_one(sql, params)
    if res[0] > 0:
        return '有'
    else :
        return '无'

def isQualified(vehicle_num):
    sql = "select check_result from (select decode(q.bischeckout, 1, '合格', '不合格') check_result, row_number() over (partition by VEHICLE_NUM order by ctime desc nulls last) nums from HB_VEHICLE_CHECK_QUALIFIED q where q.VEHICLE_NUM = :vehicle_num ) s where s.nums = 1";
    params = {
        'vehicle_num': vehicle_num
    }
    res = dbUtils.get_one(sql, params)
    if res:
        return res[0]
    return '无复检纪录'

if __name__ == '__main__':
    file = "leaseVehicle.xlsx"
    data = pd.read_excel(file)
    # print(data)
    # print(len(data))
    data_len = len(data)
    print(dir(data))
    for index, row in data.iterrows():
        vehicle_num = row['车牌号']
        if (isinstance(vehicle_num, str) and len(vehicle_num.strip()) > 0):
            print(vehicle_num)
            try:
                hasEnvCheckRecordRes = hasEnvCheckRecord(vehicle_num)
                isQualifiedRes = isQualified(vehicle_num)
                data.loc[index, '是否有环检纪录'] = hasEnvCheckRecordRes
                data.loc[index, '是否复检合格'] = isQualifiedRes
            except Exception:
                print("vehicle_num get error: " + str(vehicle_num))
                continue
    DataFrame(data).to_excel('res.xlsx', sheet_name='Sheet1', index=False, header=True)