#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 2020-7-20
# Dasmz

import requests
import re


def get_target(aURL):
    """
        return [(ip:port), (ip:port), ...]
    """
    try:
        pttn = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})'
        aHeader = {"User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7"}
        res = requests.get(url = aURL, headers = aHeader, timeout = 8)
        xMatch = re.findall(pttn, res.content.decode('utf-8'))
        if len(xMatch) > 1:
            return xMatch
        else:
            return "NOTFOUND"
    except Exception as e:
        print(e)
        return "NOTFOUND"
