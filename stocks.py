myList=['AAPL','MSFT',{'Attr1','Test2'},'F']
print(myList)
myList.append('GOOG')
print(myList)
myList.insert(2,'QCOM')
print(myList)
# x=sorted(myList)
# print(x, myList)
# x.pop(2)
# print(x, myList)
y='MSFT'
if y in myList:
    print(y, "IS IN THE LIST!")

myList2=['AAPL','MSFT',{'Attr1','Test2'},'F']
print(myList2[2])