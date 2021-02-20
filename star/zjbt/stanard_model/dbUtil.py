#!/usr/bin/env python3
#coding: utf-8

import pymysql

def get_conn():
    # conn = pymysql.connect(
    #     host='49.233.142.128',
    #     port=30461,
    #     user='wwwuser',
    #     passwd='Star7980A',
    #     db='ruoyi')
    conn = pymysql.connect(
        host='172.26.73.50',
        port=33307,
        user='wwwuser',
        passwd='Star7980A',
        db='ruoyi')
    return conn

def close_conn(conn):
    if conn:
        conn.close()


def get_cursor(conn):
    return conn.cursor()

def fetchone(cursor, sql, params ={}):
    print(dir(cursor))
    cursor.execute(sql)
    res = cursor.fetchone()
    return res

def fetchall(cursor, sql, params = {}):
    cursor.execute(sql)
    return cursor.fetchall()

def update(cursor, sql):
    cursor.execute(sql)