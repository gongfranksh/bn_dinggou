#coding=utf-8
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder

class bn_dg_warehouse(object):
        def __init__(self,object):
            self.number=object["number"]
            self.id=object["id"]
            self.name=object["name"]
