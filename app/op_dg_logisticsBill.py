#coding=utf-8
import datetime
import json
import os

import requests
import config
from app import BN_TOKEN, daily_file_folder
from app.Js.Entity.BnDgDeliverBills import BnDgDeliverBills
from app.Js.Entity.BnDgDeliverBillsDetail import BnDgDeliverBillsDetail
from app.Js.Entity.BnDgOrderTask import BnDgOrderTask
from app.beans.bn_dg_deliverBills import bn_dg_deliverBills
from app.beans.bn_dg_deliverBillsDetail import bn_dg_deliverBillsDetail


def bn_dg_get_logisticsBill(orderNum):
    try:
        if config is not None:
            access_token = {
                'access_token': BN_TOKEN,
                'orderNum': orderNum
            }

        obj = requests.get(url=config.url_logisticsBill, params=access_token)
        rst = json.loads(obj.text)
        if rst['code']==200:
            with open(daily_file_folder + os.sep + config.cache_logisticsBill, 'wt') as f:
                f.write(json.dumps(rst['data']))
            # print(rst['data'])
            return rst['data']

        return rst
    except Exception, e:
        print(e.message)
        return None


def proc_bn_dg_order_logictics():

    tasks=BnDgOrderTask()
    billtask=BnDgDeliverBills()
    billdetailtask=BnDgDeliverBillsDetail()

    #取得待处理订单
    taskslist=tasks.get_need_trans_order_task()

    for task in taskslist:
        ordernum=task["orderNum"]
        orderid=task["orderid"]

        #取得订单的发货单
        logisticlist=bn_dg_get_logisticsBill(ordernum)
        deliverlist=logisticlist["deliverBills"]
        for deliver in deliverlist:
            deliver['orderid']=orderid
            #发货单master
            master=bn_dg_deliverBills(deliver)
            billtask.sync_dg_bills(master)

            # 发货单商品明细
            orderline=deliver["logisticsBillDetails"]
            for line in orderline:
                line['orderid']=orderid
                line['orderNum']=ordernum
                line['deliverBillid']=deliver["id"]
                detailline=bn_dg_deliverBillsDetail(line)
                billdetailtask.sync_dg_bills_detail(detailline)


        # billtask.sync_dg_bills(masterlist)


# ordernum='DH-O-20190725-248299'
#ordernum='DH-O-20190725-205679'
# bn_dg_get_logisticsBill(ordernum)
proc_bn_dg_order_logictics()
