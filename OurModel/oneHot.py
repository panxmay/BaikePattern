# -*- coding: utf-8 -*-

from sklearn import preprocessing
from folksonomy.exp.main.Pre.getNegSamples import negset,posset

# reconRawData.txt 为重新生成的原始数据
f = open(r'../../data/reconRawData.txt', 'r')

# 用来存放每resource的tag group
res_tagDic = {}
taglist = []
tagoht_dic = {}

def default_process():
    global taglist,tagoht_dic
    for line in f.readlines():
        lineList = line.strip().split('\t')
        res = lineList[0]
        tag = lineList[1]
        taglist.append(tag)
        if res in res_tagDic.keys():
            res_tagDic[res] = res_tagDic[res] + "|" + tag
        else:
            res_tagDic[res] = tag
    f.close()

    for key in res_tagDic.keys():
        tags = res_tagDic[key].strip().split('|')
        res_tagDic[key] = tags
    # 将负例样本加入训练集
    taglist = list(set(taglist))

    le = preprocessing.LabelEncoder()
    taglist_num = le.fit_transform(taglist)

    oht = preprocessing.OneHotEncoder(sparse=False)
    # reshape(c,d)将数据表示为c行d列的形式，其中如果d=-1,则表示为自动计算：d = 总数据/c
    tag_oht = oht.fit_transform(taglist_num.reshape(-1, 1))

    for i in range(len(taglist)):
        key = taglist[i]
        value = tag_oht[i]
        tagoht_dic[key] = value

    print("======================================= ")
    print("len of Dic(tag:one-hot) :  " + str(len(tagoht_dic)))
    print("num of tags :  " + str(len(taglist)))
    print("======================================= ")


def wiki_process():
    #  维基百科数据
    # 地理数据
    path = '../../data/data_filtered.txt'
    # 新冠数据
    # path = '../../data/covdata_filtered.txt'
    global taglist,res_tagDic,tagoht_dic
    for line in open(path, 'r', encoding='utf-8'):
        tags = line.strip().split(' ')
        if tags is None:
            continue
        if '' in tags:
            tags = tags.remove('')
        if tags is None:
            continue
        if len(tags) == 0:
            continue
        res_tagDic[tags[0]] = tags[1:]
        taglist.extend(tags)
    # 将负例样本加入训练集
    taglist.extend(negset)
    taglist.extend(posset)
    taglist = list(set(taglist))

    le = preprocessing.LabelEncoder()
    taglist_num = le.fit_transform(taglist)

    oht = preprocessing.OneHotEncoder(sparse=False)
    # reshape(c,d)将数据表示为c行d列的形式，其中如果d=-1,则表示为自动计算：d = 总数据/c
    tag_oht = oht.fit_transform(taglist_num.reshape(-1, 1))

    for i in range(len(taglist)):
        key = taglist[i]
        value = tag_oht[i]
        tagoht_dic[key] = value

def baidubaikeAndToutiao_process():
    global taglist
    # 头条和百度百科的数据
    path = '../../data/MyTagList.txt'
    path='../../data/geo.txt'
    # path = '../../data/cov.txt'
    for line in open(path, 'r', encoding='utf-8'):
        tags = line.strip().split(' ')
        if tags is None:
            continue
        if '' in tags:
            tags = tags.remove('')
        if tags is None:
            continue
        if len(tags) == 0:
            continue
        # if ' ' in tags:
        #     tags = tags.remove(' ')
        res_tagDic[tags[0]] = tags[1:]
        taglist.extend(tags)
    # 将负例样本加入训练集
    taglist.extend(negset)
    taglist.extend(posset)
    taglist = list(set(taglist))

    le = preprocessing.LabelEncoder()
    taglist_num = le.fit_transform(taglist)

    oht = preprocessing.OneHotEncoder(sparse=False)
    # reshape(c,d)将数据表示为c行d列的形式，其中如果d=-1,则表示为自动计算：d = 总数据/c
    tag_oht = oht.fit_transform(taglist_num.reshape(-1, 1))

    for i in range(len(taglist)):
        key = taglist[i]
        value = tag_oht[i]
        tagoht_dic[key] = value



wiki_process()
# baidubaikeAndToutiao_process()
if __name__ == '__main__':
    print('ontHot')

