#coding=utf-8
import json
import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN


def bn_dg_pull_order():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                # 'loadDetail':'true',
                # 'loadRemark':'true',
                # 'status':'5'
            }

        obj = requests.get(url=config.url_order, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None

def bn_dg_pull_order_all():
    try:
        # outStorageTime        出库日期
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                # 'status':'4,5'
                # 'loadDetail':'true',
                # 'loadRemark':'true',
                # 'status':'5'
            }

        obj = requests.get(url=config.url_order_all, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None

def bn_dg_pull_order_detail():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'orderNum':'DH-R-20190722-347209',
                'status':'4,5'
            }

        obj = requests.get(url=config.url_order_detail, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None

# print(bn_dg_pull_order_detail())
# print(bn_dg_pull_order())
# print(json.dumps(bn_dg_pull_order(),ensure_ascii=False))
# json=bn_dg_pull_order()

print(Bn_Json_Message(bn_dg_pull_order_all()))
# print(Bn_Json_Message(bn_dg_pull_order()))
# print(Bn_Json_Message(bn_dg_pull_order_detail()))

orderlist=bn_dg_pull_order_all()
print orderlist
