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
from app.beans.bn_dg_order import bn_dg_order


def bn_dg_pull_order():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                # 'loadDetail':'true',
                # 'loadRemark':'true',
                # 'status':'5'
            }

        obj = requests.get(url=config.url_order, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None

def bn_dg_pull_order_all():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'loadLog':'true',
                'loadDetail':'true',
                'loadRemark':'true'
            }

        obj = requests.get(url=config.url_order_all, params=access_token)
        rst = json.loads(obj.text)
        if rst['code']==200:
            with open(daily_file_folder + os.sep + config.cache_order, 'wt') as f:
                f.write(json.dumps(rst['data']["items"]))
            return rst['data']["items"]
        return rst
    except Exception, e:
        print(e.message)
        return None

def bn_dg_pull_order_daily(procdate):
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'loadLog':'true',
                'loadDetail':'true',
                'loadRemark':'true',
                "type":'1,2',
                'beginDate':procdate.strftime('%Y-%m-%d'),
                'endDate':procdate.strftime('%Y-%m-%d')
            }

        # obj = requests.get(url=config.url_order_all, params=access_token)
        obj = requests.get(url=config.url_order_all, params=access_token)
        rst = json.loads(obj.text)
        if rst['code']==200:
            with open(daily_file_folder + os.sep + config.cache_order, 'wt') as f:
                f.write(json.dumps(rst['data']["items"]))
            return rst['data']["items"]
        return rst
    except Exception, e:
        print(e.message)
        return None


def bn_dg_pull_order_detail():
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'orderNum':'DH-R-20190722-347209',
                'status':'4,5'
            }

        obj = requests.get(url=config.url_order_detail, params=access_token)
        rst = json.loads(obj.text)
        return rst
    except Exception, e:
        print(e.message)
        return None

def proc_order_daily():
    for i in range((config.period['end'] - config.period['begin']).days + 1):
        procdate = config.period['begin'] + datetime.timedelta(days=i)
        print(procdate.strftime('%Y-%m-%d'))
        tasksjson=bn_dg_pull_order_daily(procdate)
        ordermodels=load_order_2_model(tasksjson)
        ordertask=BnDgOrderTask()
        ordertask.sync_orders(ordermodels)
        # print(tasks)

def load_order_2_model(orderlist):
    orders=[]
    for od in orderlist:
        one=bn_dg_order(od)
        orders.append(one)
    return orders




proc_order_daily()

