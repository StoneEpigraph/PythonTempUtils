#! /usr/bin/env python3
# coding:utf-8

import cx_Oracle
import yaml



class OracleDbUtil:
    def __init__(self, db_host, db_name, db_username, db_password, db_port=1521):
        self.host = db_host
        self.port = db_port
        self.name = db_name
        self.username = db_username
        self.password = db_password


        self.pool = cx_Oracle.SessionPool(user=self.username, password=self.password,
                                     dsn=self.host + ':' + str(self.port) + '/' + self.name, min=2,
                                     max=15, increment=1, encoding="UTF-8")

    def get_conn(self):
        conn = self.pool.acquire()
        return conn

    def get(self, sql, params={}):
        conn = self.get_conn()
        cursor = conn.cursor()
        return cursor.execute(sql, params).fetchall()

    def get_one(self, sql, params={}):
        import os
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        conn = self.get_conn()
        cursor = conn.cursor()
        res = cursor.execute(sql, params).fetchone()
        self.pool.release(conn)
        return res


    def update(self, sql, params={}):
        import os
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        conn = self.get_conn()
        cursor = conn.cursor()
        res = cursor.execute(sql, params)
        conn.commit()
        return res



if __name__ == '__main__':
    conf = yaml.load(open("../../bjvm/conf/bjvm.yaml"))
    db_host = conf['database']['db_host']
    db_name = conf['database']['db_name']
    db_username = conf['database']['db_username']
    db_password = conf['database']['db_password']
    db_port = conf['database']['db_port']

    dbUtils = OracleDbUtil(db_host, db_name, db_username, db_password)
    conn = dbUtils.get_conn();
    sql = '''
    select enterprise_name, region, check_time,to_char(wmsys.wm_concat(mgr_name)) person, check_result from (
        select ver.enterprise_name, dd.code_name region, to_char(d.check_time, 'yyyy-MM-dd') check_time, per.mgr_name, 
        decode(c.check_result, '0', '??????', '1', '?????????', '2', '??????????????????') check_result from tr_tmg_check_plan p 
        left join tr_tmg_check_plan_detl d on p.oid = d.plan_id
        left join tr_rpt_enterprise_verify ver on d.enterprise_id = ver.enterprise_id
        left join tc_all_dict dd on d.check_dept = dd.code_value and dd.code_type = 'GL0001'
        left join tr_tmg_check_person per on per.pk_id = d.oid
        left join tr_tmg_jg_check c on d.oid = c.plan_detl_id
        where p.year = :year and p.month = :month and c.oid is not null) group by oid, enterprise_name, region, check_time, check_result
    '''
    params = {"year": 2018, "month": "01"}
    result = dbUtils.get(sql, params)
    print(result)
