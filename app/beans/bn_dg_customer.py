#coding=utf-8
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder

class bn_dg_customer(object):
        def __init__(self,object):
            self.number=object["customertypeId"]
            self.customerStatus=object["customerStatus"]
            self.name=object["name"]
            self.address=object["address"]
            self.id=object["id"]
            self.userName=object["userName"]
            self.mobile=object["mobile"]
            self.contactor=object["contactor"]
            self.createTime=object["createTime"]

