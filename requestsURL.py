#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 2020-7-20
# Dasmz

import requests
import re
import random

import UA

def get_target(aURL):
    """
        return ['ip:port', 'ip:port', ...]
    """
    try:
        pttn = '(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5})'
        aUA = random.choice(UA.aListUA)
        aHeader = {"User-Agent": aUA}
        res = requests.get(url = aURL, headers = aHeader, timeout = 12)
        xMatch = re.findall(pttn, res.content.decode('utf-8'))
        if len(xMatch) > 1:
            return xMatch
        else:
            return "NOTFOUND"
    except Exception as e:
        print(e)
        return "NOTFOUND"


vResource = get_target(aURL = 'https://github.com/hookzof/socks5_list/blob/master/proxy.txt')
print(vResource)
