#coding=utf-8
import json
import requests
import config
from app import BN_TOKEN
import sys
sys.getdefaultencoding()

def bn_dg_get_goods_list():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'code': '2000000337074'
            }

        obj = requests.get(url=config.url_goods, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None


def bn_dg_put_goods_inventory():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                # 'goodsId':'1674534537',
                'goodsCode': '2000000337074',
                'inventory': '18'
            }

        obj = requests.post(url=config.url_goods_inventory, params=access_token)
        rst = json.loads(obj.text)

        access_token['goodsCode'] = '2000000306889'
        access_token['inventory'] = 19
        obj = requests.post(url=config.url_goods_inventory, params=access_token)
        return rst
    except Exception, e:
        print(e.message)
        return None


def bn_dg_put_goods_batch_inventory():
    try:
        warehouseId=3264589

        pt_list=[{'goodsCode': 2000000337074, 'inventoryCount': 180},
                 {'goodsCode': 2000000306889, 'inventoryCount': 118},
                 {'goodsCode': 2000000171227, 'inventoryCount': 60}
                 ]

        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'warehouseId': warehouseId,
                'productEntries': str(pt_list)
            }

        obj = requests.post(url=config.url_goods_inventory_batch, params=access_token)
        rst = json.loads(obj.text)
        print obj.url

        if rst['code']==200:
            print(rst['message'])
            return rst['message']
        else:
            print(rst['message'])
            return None

    except Exception, e:
        print(e.message)
        return None


# print(bn_dg_get_goods_list())
# bn_dg_put_goods_inventory()
bn_dg_put_goods_batch_inventory()
