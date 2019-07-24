#coding=utf-8
import datetime
import json
import os
import time

import requests
import config
from Models.Bn_DgToken import BN_DG_Token


def bn_dg_get_token():
    try:
        if config is not None:
            obj = requests.get(url=config.url_token, params=config.credential_userinfo)
            rst = json.loads(obj.text)
            token = BN_DG_Token(rst)
            return token
    except Exception, e:
        print(e.message)
        return None


def Bn_Json_Message(para_in):
    return json.dumps(para_in, ensure_ascii=False)



def make_dir(daily_file_folder):
    path = daily_file_folder.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def bn_timestamp_to_date(ymd):
    tmp_ymd = ymd

    # 毫秒级别时间戳
    if len(str(ymd)) == 13:
        tmp_ymd = ymd / 1000

    time.localtime(tmp_ymd)
    date_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tmp_ymd))
    day = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    # day = day - datetime.timedelta(hours=8)
    return day

