import csv

orderitems='/Users/it-mngr/Documents/python1/orderitems-all.csv'

lc=0
lines=[]
orders=set()
with open(orderitems, encoding='utf-8', newline='') as data:
    # header=data.readline()

    reader=csv.DictReader(data)
    for row in reader:
        lc=lc+1
        # created_at,order_id,product_id,name,price, quantity = row.split(',')
        lines.append(row)
        print(row)

print("Number of lines : ",lc)

for x in lines:
    orders.add(x['order_id'])

print("The number of orders=", len(orders))