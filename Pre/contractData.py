import re

path1 = '../../data/toutiao.txt'
path2 = '../../data/baidubaike.txt'
path3 = '../../data/MyTagList.txt'

caList = set()
with open(path1,'r',encoding = 'utf-8') as f:
    for line in f:
        caList.add(line.strip().split(';;;;||;;;;')[0])
with open(path2,'r',encoding = 'utf-8') as f:
    for line in f:
        caList.add(line.strip().split(';;;;||;;;;')[0])
# print(len(caList))

gap = ' '
ca_data = {}
for ca in caList:
    string = ca
    hypos = set()
    with open(path1, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().split(';;;;||;;;;')[1] == ca and line.strip().split(';;;;||;;;;')[0]!= ca:
                # string = string +' '+ line.strip().split(';;;;||;;;;')[0]
                hypos.add(line.strip().split(';;;;||;;;;')[0])
    with open(path2,'r',encoding = 'utf-8') as f:
        for line in f:
            if line.strip().split(';;;;||;;;;')[0] == ca and line.strip().split(';;;;||;;;;')[1]!= ca:
                # string = string + ' ' + line.strip().split(';;;;||;;;;')[1]
                hypos.add(line.strip().split(';;;;||;;;;')[1])
    ca_data[ca] = hypos

f = open(path3,'w+',encoding = 'utf-8')
for ca in ca_data:
    if len(ca_data[ca])==0:
        continue
    line = ca
    for c in ca_data[ca]:
        line = line +' ' + c
    f.write(line+'\n')
f.close()
