# -*- coding: utf-8 -*-

f = open(r'C:\Users\mengyi\Desktop\result/word.txt', 'r')

li = []
for line in f.readlines():
    if(line.strip() != ""):
        line = line.strip().split(' ')
        for i in range(len(line)):
            li.append(line[i])
    else:
        continue

li_one = list(set(li))
print ("word中的单词个数： " + str(len(li_one)))

f.close()

#####################################
# 根据过滤的421个tag过滤原数据集
# 得到223140条信息
# file中的信息： content_id / tag / 
######################################
"""

of = open(r'C:\Users\mengyi\Desktop\result\t/fileReplace.txt','r')
os = open(r'C:\Users\mengyi\Desktop\result\file.txt','a')
sum =0
for line in of.readlines():
    linelist = line.strip().split('\t')
    tag = linelist[1]
    resource = linelist[2]
    for i in range(len(li_one)):
        word = li_one[i]
        if(cmp(word.lower(),tag) == 0):
            sum += 1
            os.write(resource + '\t' + tag + '\n')
print "根据word从原始数据总抽取 : " + str(sum)
of.close()
os.close()
"""