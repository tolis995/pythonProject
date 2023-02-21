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
test1 = models.execute_kw(db, uid, password, 'sale.order.line', 'fields_get', [])
fields=[]
for x in test1:
    fields.append(x)
    print(x)
print('*' * 40)
print(fields)
print(len(fields))

#
# ids = models.execute_kw(db, uid, password, 'sale.order.line', 'search', [[['create_date', '>', '2023-02-14']]])
ids = models.execute_kw(db, uid, password, 'sale.order.line', 'search', [[['create_date', '>', '2022-12-31']]],{'limit' : 10})
test2 = models.execute_kw(db, uid, password, 'sale.order.line', 'read', [ids],
                          {'fields': ['order_id', 'name', 'price_total']})
#
print(ids)
ec=0
value=0
exceptions=['[Delivery_007] Delivery Charges', '10.0 EUR discount on total amount']
for x in test2:
    print(x['price_total'])
    if x['name'] not in exceptions:
        ec=ec+1
        value=value+x['price_total']


print("Products found in exception =", ec)
print("Total value =", round(value, 2))
