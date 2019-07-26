import datetime
import json
import os

import requests
import config
from app import BN_TOKEN, daily_file_folder
from app.Js.Entity.BnDgDeliverBills import BnDgDeliverBills
from app.Js.Entity.BnDgOrderTask import BnDgOrderTask
from app.beans.bn_dg_deliverBills import bn_dg_deliverBills


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
    taskslist=tasks.get_need_trans_order_task()
    for task in taskslist:
        ordernum=task["orderNum"]
        orderid=task["orderid"]
        logisticlist=bn_dg_get_logisticsBill(ordernum)
        masterlist=[]
        deliverlist=logisticlist["deliverBills"]
        # print('\n\n'+ordernum+'=====> orderid=====>'+str(orderid))
        for deliver in deliverlist:
            # branch=deliver["warehouse"]
            # branchcode=branch["number"]
            # branchname=branch["name"]
            # print(str(deliver["id"])
            #       +'=====>'+deliver["billNum"]
            #       +'=====>'+deliver["creatorName"]
            #       # +'=====>'+deliver["signTime"]
            #       +'=====>'+branchcode
            #       +'=====>'+branchname
            #       +'=====>'+deliver["createTime"]
            #       +'=====>'+deliver["deliverTime"]
            #       +'=====>'+deliver["deliverTime"]
            #       +'status=====>'+str(deliver["status"])
            #       +'=====>'+str(deliver["money"])
            #       )
            # customer=deliver["customer"]
            # print('customer'+'***'
            #       +' code=====>'+customer["code"]
            #       +' id=====>'+str(customer["id"])
            #       +' companyUserName=====>'+customer["companyUserName"]
            #       +' companyUserId=====>'+str(customer["companyUserId"])
            #       +' realName=====>'+customer["realName"]
            #       +' name=====>'+customer["name"]
            #       )

            # master=bn_dg_deliverBills()
            deliver['orderid']=orderid
            master=bn_dg_deliverBills(deliver)
            masterlist.append(master)
            orderline=deliver["logisticsBillDetails"]
            for line in orderline:
                print(str(line["id"])
                        + '=====>' +str(line["productCode"])
                        + '=====>' +line["productName"]
                        + '=====>' +str(line["mainCount"])
                        + '=====>' +str(line["count"])
                        + '=====>' +str(line["mainPrice"])
                        + '=====>' +str(line["price"])
                        + '=====>' +str(line["money"])
                        + '=====>' +str(line["money"])
                      )
        billtask.sync_dg_bills(masterlist)


# ordernum='DH-O-20190725-248299'
#ordernum='DH-O-20190725-205679'
# bn_dg_get_logisticsBill(ordernum)
proc_bn_dg_order_logictics()
