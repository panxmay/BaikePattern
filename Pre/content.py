# -*- coding: utf-8 -*-

f = open(r'C:\Users\mengyi\Desktop\result\file_filter.txt','r')
s = open(r'C:\Users\mengyi\Desktop\result\file_res_tag.txt','a')

li = []
for line in f.readlines():
    lineList = line.strip().split('\t')
    li.append(lineList[2])
    s.write(lineList[2] + '\t' + lineList[1] + '\n')

a = list(set(li))
a.sort()
print (a)
