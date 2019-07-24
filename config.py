# -*- coding: utf-8 -*-

#连接用户信息
# userName='15221248326'
import datetime

userName='312107511'
password='100200'
client_id='6230830'
client_secret='b7rRaQdUwnOqGH2mGRQjqkjQMijwbc67'
grant_type='client_credentials'
scope='basic'

#连接用户信息--申请
credential_userinfo = {
    'userName': userName,
    'password': password,
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': grant_type,
    'scope': scope,
}

url_base='http://api.dinghuo123.com/v2/'

#认证令牌
url_token=url_base+'oauth2/token'

#订单
url_order=url_base+'order/pull_order.json'
url_order_all=url_base+'order/order_all_list.json'
url_order_detail=url_base+'order/order_detail.json'



#商品类别列表
url_goods_type=url_base+'goods/goods_type_list.json'

#商品
url_goods=url_base+'goods/goods_list.json'

#库存列表
url_warehouse=url_base+'inventory/warehouse.json'

#商品库存修改
url_goods_inventory=url_base+'goods/goods_inventory.json'


cache_warehouse='warehouse.json'
cache_order='order.json'


period={'begin':datetime.datetime.now()- datetime.timedelta(days=5),'end':datetime.datetime.now()}


