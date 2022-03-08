#! /usr/bin/env python
#coding:utf-8

import os
import time
from OracleDbUtil import OracleDbUtil

db_host = "172.24.20.100"
db_name = "bgtp"
db_username = "xiuguan"
db_password = "TpKIbBl5ceDA"

MIN_ALARM_COUNT = 150000


dbUtils = OracleDbUtil(db_host, db_name, db_username, db_password)

# 获取所有上报的维修车次数
def get_no_upload_record_count():
    sql = "select count(*) from da_repair_record r where r.IS_REPORT = 0"
    res = dbUtils.get_one(sql)
    return res[0]

if __name__ == '__main__':
    no_upload_count = get_no_upload_record_count()
    if no_upload_count > MIN_ALARM_COUNT:
        os.system("echo %s 有未上传的电子健康档案数据量 %d >> statistics_log.log\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), no_upload_count))
        os.system("echo %s Exception 未上传电子健康档案数据超量 >> statistics_log.log\n" % time.strftime("%Y-%m-%d %H:%M:%S"))
        raise Exception("未上传电子健康档案数据超量")
    else:
        os.system("echo %s 有未上传的电子健康档案数据量 %d >> statistics_log.log\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), no_upload_count))

