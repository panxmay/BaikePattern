# -*- coding: utf-8 -*-

from folksonomy.exp.main.OurModel.oneHot import res_tagDic, tagoht_dic  # tagoht_dic tag以及对应的one-hot
import numpy as np
import random

triple_pos = []

def default_process():
    f = open(r'../../data/hyperTagList.txt', 'r')
    # triple_pos存放所有的上下位pair
    triple_pos = []  # 正例三元组(目前只有hyper和hypon)

    for line in f.readlines():
        lineList = line.strip().split(' ')
        hyper = lineList[0]
        tags = lineList[1:len(lineList)]

        for i in range(len(tags)):
            item = []
            item.append(hyper)
            item.append(tags[i])
            # print (item)
            # 此时的item中只有上，下位词
            triple_pos.append(item)

    f.close()

    print("*************************************************")
    print("上，下位词二元组共有 ：%d 组 " % len(triple_pos))

def wiki_process():
    # 地理数据
    path = '../../data/data_filtered.txt'
    # 新冠数据
    # path = '../../data/covdata_filtered.txt'
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            tags = line.strip().split(' ')
            if tags is None:
                continue
            if '' in tags:
                tags = tags.remove('')
            if len(tags) == 0:
                continue
            item = []
            item.append(tags[0])
            item.append(tags[1])
            triple_pos.append(item)

def baidubaikeAndToutiao_process():
    path = '../../data/MyTagList.txt'
    path='../../data/geo.txt'
    path = '../../data/cov.txt'
    with open(path, 'r', encoding='utf-8') as f:
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
            for i in range(1, len(tags)):
                item = []
                item.append(tags[0])
                item.append(tags[i])
                triple_pos.append(item)

wiki_process()
# baidubaikeAndToutiao_process()

add = 0
for i in range(len(triple_pos)):
    hyper = triple_pos[i][0]
    hypon = triple_pos[i][1]
    context = []
    for key in res_tagDic.keys():
        # 获取每一个key对应的tag group
        value = res_tagDic[key]
        flag = (hyper in value) and (hypon in value)
        if (flag == True):
            for j in range(len(value)):
                if (value[j] != hyper and value[j] != hypon):
                    context.append(value[j])
    context = list(set(context))

    if (len(context) != 0):
        add += 1
    triple_pos[i].append(context)

train_pos = []
# train_pos的元素为（in,out）
for i in range(len(triple_pos)):
    hyper = triple_pos[i][0]
    hypon = triple_pos[i][1]
    context = triple_pos[i][2]

    # 上下位的one-hot向量表示
    hyper_oht = tagoht_dic[hyper]
    hypon_oht = tagoht_dic[hypon]

    context_oht = []  # 存所有context的one-hot
    item = []
    for tag in context:
        tag_oht = tagoht_dic[tag]
        context_oht.append(tag_oht)

    hypon_oht = len(context_oht) * hypon_oht
    context_oht.append(hypon_oht)  # 输入为hypon和context
    context_oht = np.array(context_oht)

    in_pos = np.sum(context_oht, axis=0)
    out_pos = hyper_oht

    item.append(in_pos)
    item.append(out_pos)
    train_pos.append(item)
train_pos = np.array(train_pos)

print(type(train_pos[1]))
print(len(train_pos[0]))
print("model input data(train_pos) shape: " + str(train_pos.shape))
print("*************************************************")

# 所有训练数据 train_pos + train_neg
train = []
train.extend(train_pos)
random.shuffle(train)  # 打乱顺序

if __name__=='__main__':
    print('trainData')
