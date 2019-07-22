import json
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


