import json
import csv
filename = '/Users/it-mngr/Documents/Python/tookan4.csv'

with open(filename , encoding='utf-8', newline ='') as user_file:
    line=user_file.readline().split(',')
    for x in line:
        print(x)
    # test=json.load(line)
    # line=user_file.readline().strip('\ufeff')
    # line=line.strip('\"')
    print(line)

