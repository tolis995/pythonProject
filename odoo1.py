import csv
import xmlrpc.client
import json

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
test1 = models.execute_kw(db, uid, password, 'sale.order', 'fields_get', [])
for x in test1:
    print(x)
print('*' * 40)
test3=['user_id', 'rabbit_id', 'date_order', 'margin', 'margin_percent', 'amount_total', 'invoice_status', 'state']
ids = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['margin_percent', '>', 0]]])
test2 = models.execute_kw(db, uid, password, 'sale.order', 'read', [ids],
                          {'fields': ['user_id', 'rabbit_id', 'date_order'
                              , 'margin', 'margin_percent', 'amount_total','amount_untaxed','amount_tax', 'invoice_status', 'state', 'order_line']})
print(ids)
fields=['user_id', 'rabbit_id', 'date_order', 'margin', 'margin_percent', 'amount_total','amount_untaxed','amount_tax', 'invoice_status', 'state']
# filename='E:\Python\PycharmProjects\pythonProject4\odoomargin.csv'
filename='/Users/it-mngr/Documents/python1/odoomargin.csv'
with open(filename,'w', encoding='utf-8', newline='') as data:
    writer=csv.DictWriter(data,fieldnames=test1)
    writer.writeheader()
    writer.writerows(test2)

    # for x in test2:
    #     writer.writerow(x)


# ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['name', '=', 'Απόστολος Karkalis' ]]], {'limit': 1})
# # [record] = models.execute_kw(db, uid, password, 'res.partner', 'read', [ids])
# test2=models.execute_kw(db, uid, password, 'res.partner', 'read', [ids], {'fields': ['name', 'country_id', 'comment']})
# print(ids)
# print(test2)
# ids1 = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['invoice_status' , '=', 'invoiced']]], {'limit': 10})
# test4=models.execute_kw(db, uid, password, 'sale.order', 'read', [], {'fields': ['user_id', 'rabbit_id', 'name', 'date_order','invoice_count','order_line','amount_total','amount_undiscounted','branch_id','warehouse_id']})

# for c in test4:
#     print(c)
