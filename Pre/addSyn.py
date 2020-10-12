# -*- coding: utf-8 -*-

from .addHyper import dic
import random
import matplotlib.pyplot as plt

f = open(r'C:\Users\mengyi\Desktop\result/syn.txt', 'r')
print ("------------------------------------------")

synList = []   # 存同义词list
for line in f.readlines():
    lineList = line.strip().split(' ')
    synList.append(lineList)
print ("同义词组有：" + str(len(synList)))

f.close()

#########################
## 添加同义词
#########################

threshold = 0.5
add = 0
nList = []
for i in range(len(synList)):  #遍历所有synList
    tags = synList[i]
    fflage = False
    for key in dic.keys():
        flag = False
        key_tags = dic[key]
        comTags = list(set(tags) & set(key_tags))
        #print comTags
        ############################
        ## 无论交集中有几个tag，只按照概率添加一次，由于多次添加syn是重复的
        ##########################
        if(len(comTags) != 0):
            #print comTags
            prob = random.random()
            #print prob
            
            if(prob > threshold) :  #添加
                flag = True
                fflage = True
                add += 1
                #print "before tags: " + str(key_tags)
                if(len(tags) > 4):  #随机添加
                    addNum = random.randint(1,len(tags))
                    index = []
                    n = 0
                    while(n < addNum):
                        randIndex = random.randint(0,len(tags)-1)
                        if(randIndex not in index):    # 如果随机的下标数在index中已经存在，就再次随机。
                            index.append(randIndex)
                            n += 1
                        else:
                            continue
                    for j in range(len(index)):
                        key_tags.append(tags[index[j]])
                else: #全部添加
                    for j in range(len(tags)):
                        key_tags.append(tags[j])
            #print "after tag: " + str(key_tags)
            dic[key] = key_tags
        else:
            continue
    if(fflage == False):
        nList.append(tags)
        
print ("共添加同义词： " + str(add))
print ("未使用的同义词组： " + str(len(nList)))
#####################################
# 对所有添加上下位以及同义词的数据去重
#################################
li = [] 
for key in dic.keys():
    tags = list(set(dic[key]))
    for i in range(len(tags)):
        li.append(tags[i])
    dic[key] = tags
    
li_set = list(set(li))

###################
# 将拓展之后的resource_tag过滤
# 将tag数目大于2的存储下来
###################

dic_filter = {}   #存过滤之后的数据

for key in dic.keys():
    tags = dic[key]
    if(len(tags) > 2):
        dic_filter[key] = tags
        

print ("=========================")
print ("包含不重复单词： " + str(len(li_set)))
print ("最终数据有：" + str(len(dic)))
print  ("过滤之后的最终数据： " + str(len(dic_filter)))
print ("=========================")

dic_sta = {}
tag = []
for key in dic_filter.keys():
    tags = dic_filter[key]
    l = len(tags)
    for i in range(l):
        tag.append(tags[i])
    if(dic_sta.has_key(l)):
        dic_sta[l] = dic_sta[l] + 1
    else:
        dic_sta[l] = 1
        
tag_list = list(set(tag))
print (dic_sta)
print ("tag:" + str(len(tag_list)))


####
###画图显示resource的tag数目分布情况
x = []
y = []
for key in dic_sta.keys():
    x.append(key)
    y.append(dic_sta[key])


print (x)
print (len(x))
print (y)
plt.scatter(x[:14],y[:14])

plt.show()

###########################
## 重建原始数据
## content - tag
###########################

s = open(r'../data/reconRawData.txt', 'a')
sum = 0
for key in dic_filter.keys():
    tags = dic_filter[key]
    for i in range(len(tags)):
        s.write(str(key) + '\t' + tags[i] + '\n')
        sum += 1
print ("")
    














