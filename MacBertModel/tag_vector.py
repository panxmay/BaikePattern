# -*- coding: utf-8 -*-
from BaikePattern.MacBertModel.FullConenctionModel import weight1,summary_dict
import numpy as np

tag_vec = {}
print ("weight1 shape:" + str(weight1.shape))
my = np.matrix(weight1)

# tagoht_dic为每一个key与其one hot向量组成的字典
for key in summary_dict.keys():
    tagoht = summary_dict[key]
    mx = np.matrix(tagoht)
    x = mx * my
    # print(x.shape)
    vec = np.asarray(mx * my)[0]
    tag_vec[key] = vec

# print (tag_vec)


