# -*- coding: utf-8 -*-
from .dataPre import content_tag_filte
import random

f = open(r'../data/hyperTagList.txt','r')

# 存hyper以及其下位词list
hyperTagList = []
for line in f.readlines():
    if len(line.strip()):
        linelist = line.strip().split(' ')
        hyperTagList.append(linelist)


print ("上下位关系的list有： " + str(len(hyperTagList)))
print ("原始content-tag组有： " + str(len(content_tag_filte)))

###---------------------------------------------------------------
# 对原始content-tag组的content进行排序
keys = content_tag_filte.keys()
keys.sort()    # content最后一个是9982965
#print keys

############################################################
## 对原始content-tag组进行拓展
##### 根据上位词添加下位词
## 如果原始content-tag组中有上位词，则随机的选择是否添加是否添加新的下位词以及添加几个下位词
######## 1. 对于含有上位词的content-tag组，随机一个值和阈值进行比较，大于给定阈值，则添加，否则，不添加
######## 2. 对于经判断要添加下位词的content-tag组，根据下位词的总数，随机产生一个值，即添加几个下位词。
## 如果原始content-tag组没有上位词，则新生成一个content-tag组
######## 1. content为末尾的content + 10
######## 2. 添加词的个数为3个或以上
######## 3. 如果下位词个数小于3则全部添加
############################################################
threshold = 0.5
lenHyper = len(hyperTagList)
OutOldData = 0  #有多少hyper已存在与原始数据中
inoldData = 0
nonUse_hyper_list= []  #存放不存在的hyper的list(只有hyper)
changeNum = 0 #添加的条目数

for i in range(lenHyper):  # 遍历每一个tagPair
    hyper = hyperTagList[i][0]
    tagNum = len(hyperTagList[i]) - 1  #tagNum为当前hyper的下位词总数
    flag = False  #用于判断多少个hyper存在于原始数据中
    
    for key in content_tag_filte.keys():    #遍历字典中的每一个content-tags组
        # tags为 key 对应的标签组（原始标签组）
        tags = content_tag_filte[key]
        #print "before tags: "  + str(tags)
        
        # 判断上位词hyper是否存在于当前content对应的标签组中
        # 如果存在，则看具体情况添加下位词
    
        if hyper in tags:
            flag = True   
            # addProb为随机的添加概率，根据此概率判断是否添加下位词
            addProb =random.random()
            #print addProb

            # 是否要给该条content-tags添加下位词 --> 判断添加概率是否大于阈值
            # 添加概率大于阈值，则添加下位词
            if(addProb >= threshold):
                changeNum += 1
                # 如果下位词总数 tagNum 少于3个，全部添加
                if(tagNum < 3):
                    for j in range(tagNum):
                        tags.append(hyperTagList[i][j+1])            
                # 如果下位词总数 tagNum 多于或者等于3个，选择性添加
                else: 
                    # addNum表示添加几个下位词 
                    addNum = random.randint(1,tagNum)
                    # 随机 addNum 个index
                    index = []
                    n = 0
                    while(n < addNum):
                        randIndex = random.randint(1,tagNum)
                        if(randIndex not in index):    # 如果随机的下标数在index中已经存在，就再次随机。
                            index.append(randIndex)
                            n += 1
                        else:
                            continue
                    #给key对应tags添加index对应的tagPair中的word
                    for j in range(len(index)):
                        tags.append(hyperTagList[i][j+1])

                #print "after tags: " + str(tags)
                content_tag_filte[key] = tags
            #添加概率小于阈值，不添加下位词，跳过
            else:
                continue       
        # 如何上位词hyper不在当前content对应的标签组中，则跳过此条congtent-tags
        else:
            continue
    if(flag == False):
        OutOldData += 1
        nonUse_hyper_list.append(hyperTagList[i])
    else:
        inoldData += 1
##-----------------------------------------------------------------------------
# 上下位关系的词组有： 86
# 只有55个上位词被找到，对应的进行了添加
##-----------------------------------------------------------------------------
print ("hyper不在原始数据: " + str(OutOldData))
print ("Hyper在原始数据中: " + str(inoldData))
print ("修改数据个数: " + str(changeNum))
## -----------------------------------------------------


###################################
# 对没有使用的上位词list新建数据
###################################
newDic = {}
cur_content = 9982965

# 遍历nonUse_hyper_list的次数 --> 使用同一个上位词构建多个标签组
for round in range(100):
     # 遍历nonUse_hyper_list
    for i in range(len(nonUse_hyper_list)):  
        hyper = nonUse_hyper_list[i][0]
        tagNum = len(nonUse_hyper_list[i]) - 1
        tags = []
        tags.append(hyper)
        #全部添加
        if(tagNum < 3):  
            for j in range(tagNum):
                tags.append(nonUse_hyper_list[i][j+1]) 
        # 选取部分下位词进行添加
        else:  
            #随机选择添加下位词的个数
            addNum = random.randint(1,tagNum)  
            #随机产生下标
            index = []
            n = 0
            while(n < addNum):
                curIndex = random.randint(1,tagNum)
                if(curIndex not in index):
                    index.append(curIndex)
                    n += 1
                else:
                    continue
            #print index
            #print "-----------------"  
            # 添加addNum个下位词
            for j in range(len(index)):
                tags.append(nonUse_hyper_list[i][j+1])
            #print tags
            #print "========================="
        
        newDic[cur_content] = tags
        cur_content += 1

#print newDic
print ("新建数据： " + str(len(newDic)))

## 两个字典合并
dic = {}
dic.update(content_tag_filte)
dic.update(newDic)
for key in dic.keys():
    tags = list(set(dic[key]))
    dic[key] = tags
print ("总数据： " + str(len(dic)))
        

        
            





        




















