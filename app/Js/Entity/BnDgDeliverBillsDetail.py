# -*- coding: utf-8 -*-
from app.Js.Entity.jsEntity import JsEntity

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class BnDgDeliverBillsDetail(JsEntity):

    def __init__(self):
        JsEntity.__init_no_branchcode__(self, "bn_dg_deliverBillsDetail")


    def sync_dg_bills_detail(self,detaillist):
        # if len(detaillist)!=0:
            # for dt in detaillist:
        if detaillist is not None:
            dt=detaillist
            r01=self.seek_line_by_id(dt.id)
            if len(r01)==0:
                    self.insert_into_dg_bills_detail(dt)


    def seek_line_by_id(self,lineid):
        sql = " SELECT * FROM bn_dg_deliverBillsDetail where deliverBillDetailid =" +str(lineid)
        rst = self.get_remote_result_by_sql(sql)
        return rst

    def insert_into_dg_bills_detail(self, bl):
        insert_statment = """
            INSERT INTO dbo.bn_dg_deliverBillsDetail 
            (
            deliverBillDetailid, deliverBillid, orderid, orderNum, billNum, 
            productCode, productName, mainCount, count, mainPrice, 
            price, total_Money
            )        
            values ({0},{1},{2},'{3}','{4}',
                '{5}','{6}',{7},{8},{9},
                {10},{11}
        )
        """
        insert_statment = insert_statment.format(
            bl.id,bl.deliverBillid,bl.orderid,bl.orderNum,bl.billNum,
            bl.productCode,bl.productName,bl.mainCount,bl.count,bl.mainPrice,
            bl.price, bl.money
        )
        # print(insert_statment)
        self.execSql(insert_statment)

    def update_dg_bills_detail(self, bmt):
        pass
        # update_statment="""
        #     UPDATE dbo.bn_dg_deliverBills
        #     SET
        #         address = '{0}',
        #         sendCompanyCode = '{1}',
        #         contact ='{2}',
        #         customerId = {3},
        #         customercode = '{4}',
        #         customername ='{5}',
        #         customerrealName = '{6}',
        #         db_Money = {7},
        #         status ='{8}'
        #     where deliverBillid ={9}
        #         """
        # update_statment = update_statment.format(
        #     bmt.address,
        #     bmt.sendCompanyCode,
        #     bmt.contact,
        #     bmt.customerId,
        #     bmt.customercode,
        #     bmt.customername,
        #     bmt.customerrealName,
        #     bmt.money,
        #     bmt.status,
        #     bmt.id
        # )
        # # print(update_statment)
        # self.execSql(update_statment)

