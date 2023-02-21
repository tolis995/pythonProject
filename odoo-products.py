import csv
import xmlrpc.client


common = xmlrpc.client.ServerProxy('https://rabbit.methodoos.com/xmlrpc/2/common')
common.version()
print(common.version())

url = 'https://rabbit.methodoos.com/'
db = 'rabbit'
username = 'it-mngr@rabbitapp.co'
password = '17-mn92@0d00'
uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy(url + 'xmlrpc/2/object')

# test1=models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [])
test1 = models.execute_kw(db, uid, password, 'product.product', 'fields_get', [])
fields=[]
values=[]
for x in test1:
    fields.append(x)
    print(x)
print('*' * 40)
print(fields)
print(len(fields))
#

ids = models.execute_kw(db, uid, password, 'product.product', 'search', [[['price', '>', 0]]], {'limit':100})
# ids = models.execute_kw(db, uid, password, 'sale.order.line', 'search', [[['create_date', '>', '2022-12-31']]])
# ids = models.execute_kw(db, uid, password, 'product.product', 'search', [[['create_date', '>', '2022-12-31']]])
test2 = models.execute_kw(db, uid, password, 'product.product', 'read', [ids],
                          {'fields': ['code', 'price', 'qty_available', 'purchase_avg_price'
                              , 'total_cost', 'sales_count', 'display_name']})
#
print(ids)
# exceptions=['[Delivery_007] Delivery Charges', '10.0 EUR discount on total amount']
for x in test2:
    print(x)
