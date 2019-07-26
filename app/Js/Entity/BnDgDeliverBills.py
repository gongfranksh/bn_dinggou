# -*- coding: utf-8 -*-
from app.Js.Entity.jsEntity import JsEntity

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BnDgDeliverBills(JsEntity):

    def __init__(self):
        JsEntity.__init_no_branchcode__(self, "bn_dg_deliverBills")


    def sync_dg_bills(self,dglist):
        if len(dglist)!=0:
            for bill in dglist:
                r01=self.seek_bills_by_id(bill.id)
                if len(r01)!=0:
                    self.update_dg_bills(bill)
                else:
                    self.insert_into_dg_bills(bill)


    def seek_bills_by_id(self,billid):
        sql = " SELECT * FROM bn_dg_deliverBills where deliverBillid =" +str(billid)
        rst = self.get_remote_result_by_sql(sql)
        return rst

    def insert_into_dg_bills(self, bmt):
        insert_statment = """
        INSERT INTO dbo.bn_dg_deliverBills 
          (deliverBillid, orderid, orderNum, billNum, address, 
            sendCompanyCode, branchcode, branchname, contact, customerId, 
            customercode, customername, customerrealName, db_Money, status,
            createtime
            )
        values ({0},{1},'{2}','{3}','{4}',
                '{5}','{6}','{7}','{8}',{9},
                '{10}','{11}','{12}',{13},{14},
                '{15}'
        )
        """
        insert_statment = insert_statment.format(
        bmt.id,bmt.orderid,bmt.orderNum,bmt.billNum,bmt.address,
        bmt.sendCompanyCode,bmt.branchcode,bmt.branchname,bmt.contact,bmt.customerId,
        bmt.customercode,bmt.customername,bmt.customerrealName,bmt.money,bmt.status,
        bmt.createTime
        )
        # print(insert_statment)
        self.execSql(insert_statment)

    def update_dg_bills(self, bmt):
        update_statment="""
            UPDATE dbo.bn_dg_deliverBills
            SET 
                address = '{0}',
                sendCompanyCode = '{1}',
                contact ='{2}',
                customerId = {3},
                customercode = '{4}',
                customername ='{5}',
                customerrealName = '{6}',
                db_Money = {7},
                status ='{8}'
            where deliverBillid ={9}
                """
        update_statment = update_statment.format(
            bmt.address,
            bmt.sendCompanyCode,
            bmt.contact,
            bmt.customerId,
            bmt.customercode,
            bmt.customername,
            bmt.customerrealName,
            bmt.money,
            bmt.status,
            bmt.id
        )
        # print(update_statment)
        self.execSql(update_statment)
