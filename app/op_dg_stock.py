#coding=utf-8
import json
import os

import requests
import config
from Tools.bn_dg_tools import Bn_Json_Message
from app import BN_TOKEN, daily_file_folder
from app.Js.Entity.BnDgStock import BnDgStock
from app.beans.bn_dg_warehouse import bn_dg_warehouse
from app.op_dg_goods import bn_dg_put_goods_batch_inventory


def bn_get_need_sync_stock_list_by_branch():
    tasks = BnDgStock()
    branchlist= tasks.get_need_sync_branch()
    stock_need_update=[]
    for store in branchlist:
        stocklist=tasks.get_current_stocklist(store['braid'])
        pdlist=[]
        for item in stocklist:
            proid=item['proid']

            pd={
                'goodsCode':proid ,
                'inventoryCount':item['curqty'],
                # 'inventoryCount':str(item['curqty']),
            }
            pdlist.append(pd)
            # print(item)
        proc_stock={
            'warehouseId':store['bn_dg_warehouseid'],
            'productEntries':pdlist
        }

        stock_need_update.append(proc_stock)
    return stock_need_update

def proc_bn_dg_stock_qty():
    tasklist=bn_get_need_sync_stock_list_by_branch()
    for task in tasklist:
        str=bn_dg_put_goods_batch_inventory(task)
        print(str)

