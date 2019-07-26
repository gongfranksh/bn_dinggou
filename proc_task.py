#coding=utf-8
import datetime

import config
from app.Js.Entity.BnDgOrderTask import BnDgOrderTask
from app.op_dg_customer import bn_dg_get_customer_list, load_customer_2_model
from app.op_dg_order import bn_dg_pull_order_daily, load_order_2_model


def proc_sync_order_daily_by_createdate():
    for i in range((config.period['end'] - config.period['begin']).days + 1):
        procdate = config.period['begin'] + datetime.timedelta(days=i)
        print(procdate.strftime('%Y-%m-%d'))

        tasksjson=bn_dg_pull_order_daily(procdate)
        ordermodels=load_order_2_model(tasksjson)
        ordertask=BnDgOrderTask()
        ordertask.sync_orders(ordermodels)

        # tasks_customer = bn_dg_get_customer_list(procdate)
        # customer_model=load_customer_2_model(tasks_customer)
        # print(customer_model)




proc_sync_order_daily_by_createdate()