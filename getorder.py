import json
import os

import requests

import config
from app import BN_TOKEN, daily_file_folder


def order_test():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'loadLog':'true',
                'loadDetail':'true',
                'loadRemark':'true',
                "type":'1,2',
                # 'beginDate':procdate.strftime('%Y-%m-%d'),
                # 'endDate':procdate.strftime('%Y-%m-%d')
            }

        # obj = requests.get(url=config.url_order_all, params=access_token)
        obj = requests.get(url=config.url_order_all, params=access_token)
        rst = json.loads(obj.text)
        if rst['code']==200:
            with open(daily_file_folder + os.sep + config.cache_order, 'wt') as f:
                f.write(json.dumps(rst['data']["items"]))
            return rst['data']["items"]
        return rst
    except Exception, e:
        print(e.message)
        return None

order_test()