from Tools.bn_dg_tools import bn_dg_get_token

try:
    BN_TOKEN=bn_dg_get_token().access_token
except Exception,e:
    print(e.message)