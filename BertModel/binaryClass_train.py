# -*- coding: utf-8 -*-

import random
from BaikePattern.BertModel.FullConenctionModel import summary_dict
from BaikePattern.Pre.getNegSamples import neglist, negset,posset,poslist
from BaikePattern.BertModel.tag_vector import tag_vec

titles = ['geo','coronavirus']

# 找到负例
# 新冠数据负例设置为750，地理数据负例设置为900
neg = []
pos = []
# neg = [('病毒', '核糖病毒', 0),('醫療急症', '酸碱紊乱糖尿病', 0)]
for item in neglist:
    if item[0] in summary_dict.keys() and item[1] in summary_dict.keys():
        neg.append((item[1], item[0], 0))
for item in poslist:
    if item[0] in summary_dict.keys() and item[1] in summary_dict.keys():
        pos.append((item[1], item[0], 1))


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
