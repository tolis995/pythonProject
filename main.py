# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/it-mngr/Documents/Python/test2.csv")

df.plot(kind='hist', x = 'product_id', y = 'quantity')

plt.show()



print("hello apostolis!")

x = ("A","B","R","J","K","F","A")

print(len(x))
print(x.count("A"))

print(x.index("J"))
y=list(x)
y.sort()
x=tuple(y)
for i in x:
    print(i)


#f = open("/Users/it-mngr/Documents/Python/test2.csv", "rt")

#print(f.read())



df = pd.read_csv("/Users/it-mngr/Documents/Python/test2.csv")

#print(df.head(100))

print(df.info())
print(df.corr())