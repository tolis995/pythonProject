import csv


myfile='/Users/it-mngr/Documents/python1/AAPL1.csv'
ordersitems='/Users/it-mngr/Documents/orderitems-all.csv'
mc=0
lc=0

with open(myfile, encoding='utf-8', newline='') as data:
    reader=csv.DictReader(data)
    # lc=sum(1 for line in reader)
    print("Number of lines : ",lc)
    for row in reader:
        lc=lc+1
        print(row)
        x=row['Date'].split('-')
        print(x[1])
        if x[1]=='03':
            mc=mc+1
            print(row)
        # if row['Volume']=='61177400':
        #     print(row)
    # headers=data.readline().strip('\n\r').split(',')
    # print(f'Column Headers: {headers}')
    # reader=csv.reader(data)
    # for row in reader:
    #     print(row[0],row[1],row[6])
print("Monthly data :",mc)
print("Number of lines : ",lc)

print("This is a test : ",test(5))
print("This is a test : ",test('*'))