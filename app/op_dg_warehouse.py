#coding=utf-8
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder
from app.beans.bn_dg_warehouse import bn_dg_warehouse


def bn_dg_warehouse_list():
    rst=[]
    for wh in get_dg_warehouse_from_cache():
        w = bn_dg_warehouse(wh)
        rst.append(w)
    return rst

#按照门店代码取得分销的warehouseid
def bn_seek_warehouse(branchcode):
    warehouselist=bn_dg_warehouse_list()
    for wh in warehouselist:
        if wh.number==branchcode:
            return wh
    return None

def bn_dg_get_warehouse():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
            }

        obj = requests.get(url=config.url_warehouse, params=access_token)
        rst = json.loads(obj.text)
        if rst['code']==200:
            with open(daily_file_folder + os.sep + config.cache_warehouse, 'wt') as f:
                f.write(json.dumps(rst['data']))
            return rst['data']
    except Exception, e:
        print(e.message)
        return None

def get_dg_warehouse_from_cache():
    with open(daily_file_folder + os.sep + config.cache_warehouse, 'r') as f:
        rst=(json.load(f))
    return  rst


# wh=bn_seek_warehouse('01002')
# print(wh.id)