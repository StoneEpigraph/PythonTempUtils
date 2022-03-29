#!/usr/bin/env python3
#coding: utf-8

import pymysql
from dbutils.pooled_db import PooledDB

class MySQLUtil:

    _pool = None

    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db

    def _get_conn(self,):
        """
        获取连接，如果连接池还未初始化，那么初始化
        :return:
        """
        if self._pool is None:
            self._pool = PooledDB(creator=pymysql,
                              mincached=1,
                              maxcached=20,
                              host=self.host,
                              port=self.port,
                              user=self.user,
                              passwd=self.passwd,
                              db=self.db,
                              use_unicode=True,
                              charset="utf8",
                              cursorclass=pymysql.cursors.DictCursor)
        self._conn = self._pool.connection()
        self._cursor = self._conn.cursor()


    def fetch_all(self, sql, params):
        """
            根据sql查所有数据
        :param sql:
        :param param:
        :return:
        """
        try:
            self._get_conn()
            if params is None:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, params)
            if count > 0:
                result = self._cursor.fetchall()
            else:
                result = False
            return result
        except Exception as e:
            print(e.args[-1])
            return False
        finally:
            if self._cursor:
                self._cursor.close()
            if self._conn:
                self._conn.close()

    def fetch_one(self, sql, params={}):
        """
            根据sql查询一条数据
        :param sql:
        :param params:
        :return:
        """
        try:
            self._get_conn()
            print(self._conn)
            if params is None or len(params) < 1:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, params)
            if count > 0:
                result = self._cursor.fetchone()
            else:
                result = False
            return result
        except Exception as e:
            print(e.args[-1])
            return False
        finally:
            if self._cursor:
                self._cursor.close()
            if self._conn:
                self._conn.close()

    def execute(self, sql, params = {}):
        try:
            self._get_conn()
            if params is None or len(params) < 1:
                count = self._cursor.execute(sql)
            else:
                count = self._cursor.execute(sql, params)
            self._conn.commit()
            return count
        except Exception as e:
            print(e)
            print(e.args[-1])
            self._conn.rollback()
            return False
        finally:
            if self._cursor:
                self._cursor.close()
            if self._conn:
                self._conn.close()


if __name__ == '__main__':
    host = "152.136.97.65"
    port = 33307
    user = "shopuser"
    passwd = "Star@2022A"
    db = "lilishop"
    mysqlUtil = MySQLUtil(host, port, user, passwd, db)
    for i in range(30):
        print(mysqlUtil.fetch_one("select count(*) from li_store"))