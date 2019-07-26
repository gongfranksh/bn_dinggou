#coding=utf-8
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder

class bn_dg_deliverBills(object):
        def __init__(self,object):
            self.id=object["id"]
            self.orderNum=object["orderNum"]
            self.orderid=object["orderid"]
            self.billNum=object["billNum"]
            self.money=object["money"]
            self.createTime=object["createTime"]
            self.address=object["address"]
            self.sendCompanyCode=object["sendCompanyCode"]
            self.branchcode=object["warehouse"]["number"]
            self.branchname=object["warehouse"]["name"]
            self.contact=object["contact"]
            self.customerId=object["customerId"]
            self.customercode=object["customer"]["code"]
            self.customername=object["customer"]["name"]
            self.customerrealName=object["customer"]["realName"]
            self.status=object["status"]


