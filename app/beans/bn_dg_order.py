#coding=utf-8
import datetime
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder
from app.Js.Entity import *
from app.Js.Entity.BnDgOrderTask import BnDgOrderTask


class bn_dg_order(object):
    def __init__(self, object):
        self.orderNum = object["orderNum"]
        self.id = object["id"]
        self.status = object["status"]
        self.payStatus = object["payStatus"]
        self.signStatus = object["signStatus"]
        self.deliverStatus = object["deliverStatus"]
        self.outStorageStatus = object["outStorageStatus"]
        self.actualMoney = object["actualMoney"]
        self.Money = object["money"]
        self.createTime = object["createTime"]
        self.modifyTime = object["modifyTime"]
        self.type = object["type"]


