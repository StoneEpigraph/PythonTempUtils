#! /usr/bin/env python3
# coding:utf-8

import cx_Oracle

class OracleDbUtil:
    def __init__(self, db_host, db_name, db_username, db_password, db_port=1521):
        self.host = db_host
        self.port = db_port
        self.name = db_name
        self.username = db_username
        self.password = db_password

    def get_conn(self):
        url = self.username + '/' + self.password + '@' + self.host + ':' + str(self.port) + '/' + self.name
        conn = cx_Oracle.connect(url)
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
        return cursor.execute(sql, params).fetchone()

    def update(self, sql, params={}):
        import os
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
        conn = self.get_conn()
        cursor = conn.cursor()
        res = cursor.execute(sql, params)
        conn.commit()
        return res

