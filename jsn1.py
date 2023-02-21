import xmlrpc.client
import json
# import urllib
# # info = xmlrpc.client.ServerProxy('https://integrationrabbit.methodoos.com/').start()
# # url, db, username, password = info['host'], info['database'], info['user'], info['password']

common = xmlrpc.client.ServerProxy('https://integrationrabbit.methodoos.com/xmlrpc/2/common')
common.version()
print(common.version())
url = 'https://integrationrabbit.methodoos.com/'
db = 'integrationrabbit'
username = 'testuser'
password = 'testuser@#$'
uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy(url+'xmlrpc/2/object')
print(models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', ['read'], {'raise_exception': False}))
print(models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]]))

print(models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]]))

print(models.execute_kw(db, uid, password, 'ir.model', 'fields_get', [], {'attributes': ['string', 'help', 'type']}))

test1=models.execute_kw(db, uid, password, 'res.partner', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
print("*" * 30)
# print(test1['name'])
# print("*" * 30)
# print(test1['model'])
# print("*" * 30)
# print(test1['order'])
# print("*" * 30)
# print(test1['info'])
# print("*" * 30)

for x in test1:
    if x=='is_company':
       print(x)

ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['name', '=', 'Απόστολος Karkalis' ]]], {'limit': 1})
# [record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
test2=models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
print(ids)
print(test2)
print('/' * 40)
fs=models.execute_kw(db, uid, password, 'sale.order', 'fields_get', [])
for x in fs:
    print(x)

# test3=models.execute_kw(db, uid, password, 'sale.order', 'read', [], {'fields': ['user_id', 'invoice_status', 'amount_total', 'branch_id', 'rabbit_id']})
ids1 = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['invoice_status' , '=', 'invoiced']]])

print(ids1)

test4=models.execute_kw(db, uid, password, 'sale.order', 'read', [ids1], {'fields': ['user_id', 'rabbit_id', 'name', 'date_order','invoice_count','order_line','amount_total','amount_undiscounted','branch_id','warehouse_id']})

for c in test4:
    print(c)
# print(test4)
# for x in ids1:
#
#     print(x)

# recs=models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['id', '=', '528' ]]], {'fields': ['name', 'country_id', 'comment'], 'limit': 100})
#
# for x in recs:
#     for y in x:
#         print(y)
#     print(x)

    