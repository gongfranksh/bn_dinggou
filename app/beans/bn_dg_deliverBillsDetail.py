#coding=utf-8
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder

class bn_dg_deliverBillsDetail(object):
        def __init__(self,object):
            self.id=object["id"]
            self.orderid=object["orderid"]
            self.deliverBillid=object["deliverBillid"]
            self.orderNum=object["orderNum"]
            self.billNum=object["billNum"]
            self.productCode=object["productCode"]
            self.productName=object["productName"]
            self.mainCount=object["mainCount"]
            self.count=object["count"]
            self.price=object["price"]
            self.mainPrice=object["mainPrice"]
            self.money=object["money"]


