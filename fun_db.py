#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 2020-8-5
# Dasmz


def dataInDB(aDB, aSQL):
    try:
        conn = sqlite3.connect(aDB)
        csr = conn.cursor()
        csr.execute(aSQL)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def dataOutDB(aDB, aSQL):
    try:
        conn = sqlite3.connect(aDB)
        cur = conn.cursor()
        cur.execute(aSQL)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        print(e)
    finally:
        conn.close()
