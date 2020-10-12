# -*- coding: utf-8 -*-

from folksonomy.exp.main.OurModel.trainData import triple_pos
import random
from folksonomy.exp.main.Pre.getNegSamples import neglist, negset,posset,poslist
from folksonomy.exp.main.OurModel.model import weight2
from folksonomy.exp.main.OurModel.tag_vector import tag_vec
import numpy as np
import scipy.spatial.distance as distance


# triple_pos存放tag_sum_hot和hyper_hot向量
pos = []
# for i in range(len(triple_pos)):
#     hyper = triple_pos[i][0]
#     hypon = triple_pos[i][1]
#     cls = 1
#     item = (hyper, hypon, cls)
#     pos.append(item)

for item in poslist:
    pos.append((item[1], item[0], 1))

words = []
# 地理数据
path = '../../data/data_filtered.txt'
# 新冠数据
# path = '../../data/covdata_filtered.txt'
# path ='../../data/MyTagList.txt'
# path='../../data/geo.txt'
# path = '../../data/cov.txt'
f = open(path, 'r', encoding='utf-8')
for line in f:
    tags = line.strip().split(' ')
    if tags is None:
        continue
    if '' in tags:
        tags = tags.remove('')
    if tags is None:
        continue
    if len(tags) == 0:
        continue
    for i in range(len(tags)):
        words.append(tags[i])
words.extend(negset)
words.extend(posset)
words = list(set(words))   # 目的为了收集词汇表

# 找到负例
neg = []
num = 1
# 新冠数据负例设置为750，地理数据负例设置为900
all = 700
while(num <= all):
    index1 = random.randint(0, len(words) - 1)
    index2 = random.randint(0, len(words) - 1)
    while(index1 == index2):
        index2 = random.randint(0, len(words) - 1)
    cls = 0
    flag = False
    for i in range(len(pos)):
        pos_1 = pos[i][0]
        pos_2 = pos[i][1]
        # 找到上下位词，并过滤掉
        con1 = (pos_1 == words[index1]) and (pos_2 == words[index2])
        con2 = (pos_1 == words[index2]) and (pos_1 == words[index1])
        if((con1 or con2)):
            flag = True
            break
    if(flag):
        continue
    else:
        # 留下非上下位词，标记为负例
        item = (words[index1], words[index2], cls)
        neg.append(item)
        num += 1
neg = []
# neg = [('病毒', '核糖病毒', 0),('醫療急症', '酸碱紊乱糖尿病', 0)]
for item in neglist:
    neg.append((item[1], item[0], 0))

print("num of pos: " + str(len(pos)))
print("num pf neg: " + str(len(neg)))

train = []  # 元素为tag
for i in range(len(pos)):
    train.append(pos[i])
for i in range(len(neg)):
    train.append(neg[i])
random.shuffle(train)

train_vec = []
for i in range(len(train)):
    item = train[i]
    tag1 = item[0]
    tag2 = item[1]
    cls = item[2]
    # 得到神经网络模型的向量
    tag1_vec = tag_vec[tag1]
    tag2_vec = tag_vec[tag2]
    newItem = (tag1_vec, tag2_vec, cls)
    train_vec.append(newItem)
