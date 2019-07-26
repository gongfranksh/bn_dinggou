# -*- coding: utf-8 -*-
from app.Js.Entity.jsEntity import JsEntity


class BnDgCustomer(JsEntity):

    def __init__(self):
        JsEntity.__init_no_branchcode__(self, "bn_dg_deliverBills")




    def get_branch_all(self):
        sql= " SELECT * FROM branch WHERE BraType='0' AND Status='0' ORDER BY BraName,braid "
        rst = self.get_remote_result_by_sql(sql)
        return rst

