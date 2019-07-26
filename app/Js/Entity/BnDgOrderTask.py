# -*- coding: utf-8 -*-
from app.Js.Entity.jsEntity import JsEntity
# from app.beans import *
# from app.beans.bn_dg_order import bn_dg_order


class BnDgOrderTask(JsEntity):

    def __init__(self):
        JsEntity.__init_no_branchcode__(self, "bn_dg_order_task")

    def get_bn_dg_order_task_all(self):
        sql= " SELECT * FROM bn_dg_order_task "
        rst = self.get_remote_result_by_sql(sql)
        return rst



    def get_need_track_order_task(self):
        sql = """
          SELECT * FROM bn_dg_order_task  NeedTrack=0 AND type=1
        """
        rst = self.get_remote_result_by_sql(sql)
        return rst



    def get_need_trans_order_task(self):
        sql = """
                      SELECT * FROM 
                      bn_dg_order_task  
                      WHERE 
                      DoneFlag=0 AND deliverStatus !=0 
                  """
        rst = self.get_remote_result_by_sql(sql)
        return rst



    def sync_orders(self,orderlist):
        if len(orderlist)!=0:
            for order in orderlist:

                r01=self.seek_order_by_id(order.id)
                if len(r01)!=0:
                    self.update_dg_task(order)
                else:
                    self.insert_into_dg_task(order)


    def update_dg_task(self, odb):
        payflag = odb.payStatus

        if odb.type == 2:
            payflag = 0

        update_statment = """
              UPDATE dbo.bn_dg_order_task
                SET actualMoney = {0}
                    , order_money = {1}
                    , status = {2}
                    , payStatus = {3}
                    , signStatus = {4}
                    , outStorageStatus = {5}
                    , deliverStatus ={6}
                    , modifyTime = '{7}'
                WHERE orderid = {8}        
                """
        update_statment = update_statment.format(
            odb.actualMoney,
            odb.Money,
            odb.status,
            payflag,
            odb.signStatus,
            odb.outStorageStatus,
            odb.deliverStatus,
            odb.modifyTime,
            odb.id
        )
        # print(update_statment)
        self.execSql(update_statment)


    def insert_into_dg_task(self, odb):
        # , NeedTrack, TransFlag, DoneFlag, logdate
        #退货单补一个付款状态
        payflag=odb.payStatus

        if odb.type==2:
            payflag=0

        insert_statment = """
         INSERT INTO dbo.bn_dg_order_task 
         (
             orderid, orderNum, actualMoney, order_money, status, 
             payStatus, signStatus, outStorageStatus, deliverStatus,createTime, 
             modifyTime,type
         )
        values ({0},'{1}',{2},{3},{4},
                {5},{6},{7},{8},'{9}',
                '{10}',{11}
        )
        """
        insert_statment = insert_statment.format(
            odb.id, odb.orderNum, odb.actualMoney, odb.Money, odb.status,
            payflag, odb.signStatus, odb.outStorageStatus, odb.deliverStatus, odb.createTime,
            odb.modifyTime,odb.type)
        print(insert_statment)
        self.execSql(insert_statment)

    def seek_order_by_id(self,orderid):
        sql = " SELECT * FROM bn_dg_order_task where orderid =" +str(orderid)
        rst = self.get_remote_result_by_sql(sql)
        return rst