import json
import requests
import config
from app import BN_TOKEN


def bn_dg_pull_order():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
            }

        obj = requests.get(url=config.url_order, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None

