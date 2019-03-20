import yaml
import json
import csv
import pandas
#yaml
fopen = open("conf.yaml","r")
yamlload = yaml.load(fopen)
yamlkey = yamlload["LogFile"]["HEList"]
#print yamlkey, "\n\n"
for i in yamlkey.keys():
    if i == 'CHN':
        locyaml = yamlkey[i]
        #print (locyaml['Userid'])

#JSON --> returns dict
with open('chncox.json','r') as jf:
    jf = jf.read()
    jsonfile = json.loads(jf)
    #print jsonfile, type(jsonfile)
    for j in jsonfile.keys():
        if j == 'dayBefore':
            jdb = jsonfile[j]
            #print jdb, type(jdb)
            #print jdb['Total']

#CSV : --> returns List
with open("csvfile.csv",'r') as csvfile, open("csvfile1.csv",'wb') as csvwrite:
    csv_data = csv.reader(csvfile)
    #print type(csv_data)
    for data in csv_data:
        #print data, type(data)
        csvwr = csv.writer(csvwrite)
        csvwr.writerow(data)

#Pandas: --> returns "<class 'pandas.core.frame.DataFrame'>"
res = pandas.read_csv('data.csv')
print res, type(res)
for p in res:
    print res[p][0]

import pandas
df = pandas.read_csv('data.csv',
            index_col='Prog Lang',
            names=['Prog Lang', 'Developed By', 'Year', 'extension'])
df.to_csv('hrdata_modified.csv')



