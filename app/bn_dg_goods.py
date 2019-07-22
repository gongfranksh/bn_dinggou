import json
import requests
import config
from app import BN_TOKEN


def bn_dg_get_goods_list():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'code':'2000000337074'
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
                'goodsCode':'2000000337074',
                'inventory':'187'
            }

        obj = requests.post(url=config.url_goods_inventory, params=access_token)
        rst = json.loads(obj.text)

        access_token['goodsCode']='2000000306889'
        access_token['inventory']=111
        obj = requests.post(url=config.url_goods_inventory, params=access_token)
        return rst
    except Exception, e:
        print(e.message)
        return None


print(bn_dg_get_goods_list())
# bn_dg_put_goods_inventory()