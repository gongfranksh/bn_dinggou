# -*- coding: utf-8 -*-
from app.Js.Entity.jsEntity import JsEntity


class BnDgStock(JsEntity):

    def __init__(self):
        JsEntity.__init_no_branchcode__(self, "stock")

    def get_current_stocklist(self,branchcode):
        sql = """
                SELECT bh.bn_dg_warehouseid ,s.braid,s.proid,CAST (isnull(s.curqty,0) as int) curqty 
                FROM stock s
                LEFT JOIN branch  bh ON s.BraId=bh.braid
                WHERE s.ProId IN (
                '2000000171227',
                '2000000234861',
                '2000000234878',
                '2000000306872',
                '2000000306889',
                '2000000337074',
                '2000000337081'
                )
                AND isnull(bh.bn_dg_warehouseid,0)<> 0
                AND s.braid='{0}'
                ORDER BY bh.bn_dg_warehouseid,s.proid
        """
        sql=sql.format(branchcode)
        rst = self.get_remote_result_by_sql(sql)
        return rst



    def get_need_sync_branch(self):
        sql = """
            SELECT braid, bn_dg_warehouseid 
            FROM branch 
            WHERE isnull(bn_dg_warehouseid,0)<> 0
        """
        rst = self.get_remote_result_by_sql(sql)
        return rst