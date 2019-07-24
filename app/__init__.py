import os

from Tools.bn_dg_tools import bn_dg_get_token, make_dir

try:
    BN_TOKEN=bn_dg_get_token().access_token

    data_dir_name = 'datas'
    daily_file_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) \
                      + os.sep \
                      + data_dir_name
    print(daily_file_folder)
    make_dir(daily_file_folder)
except Exception,e:
    print(e.message)