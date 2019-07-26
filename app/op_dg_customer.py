import datetime
import json
import os

import requests
import config
from app import BN_TOKEN, daily_file_folder
from app.beans.bn_dg_customer import bn_dg_customer


def bn_dg_get_customer_list(procdate):
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                # 'beginTime':'2019-7-25',
                # 'endTime':'2019-7-26'
                'beginTime':procdate.strftime('%Y-%m-%d'),
                'endTime':(procdate+ datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            }

        obj = requests.get(url=config.url_customer, params=access_token)
        rst = json.loads(obj.text)
        if rst['code']==200:
            with open(daily_file_folder + os.sep + config.cache_customer, 'wt') as f:
                f.write(json.dumps(rst['data']["items"]))
            print(rst['data']["items"])
            return rst['data']["items"]

        return rst
    except Exception, e:
        print(e.message)
        return None


def load_customer_2_model(customerlist):
    cs=[]
    for ct in customerlist:
        one=bn_dg_customer(ct)
        cs.append(one)
    return cs


# bn_dg_get_customer_list(datetime.datetime.now()- datetime.timedelta(days=0))
# print(bn_dg_get_goods_list())
