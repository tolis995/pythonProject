import csv
def countUsersPerMonth(orders,month):
    m=''
    mc=0
    for x in orders:
        m=x['created_at'].split('/')
        if (m[1]==month):
            mc=mc+1
    return mc

orderfile='/Users/it-mngr/Documents/python1/allorders.csv'

lc=0
lines=[]
orders=set()
with open(orderfile, encoding='utf-8', newline='') as data:
    reader=csv.DictReader(data)
    for row in reader:
        lc=lc+1
        if ((row['payment_status'] == 'paid') and (row['status'] == 'delivered')):
            lines.append(row)
        print(row)

print("Number of lines : ",lc)

for x in lines:
    if ((x['payment_status']=='paid') and (x['status']=='delivered')):
        orders.add(x['id'])

print("The number of Valid orders=", len(orders))
# print(orders)
oc=0
for x in lines:
    if x['payment_status']=='paid':
        oc=oc+1

print("Number of paid order=",oc)
print(countUsersPerMonth(lines,'12'))