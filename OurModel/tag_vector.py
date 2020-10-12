# -*- coding: utf-8 -*-
from folksonomy.exp.main.OurModel.model import weight1
from folksonomy.exp.main.OurModel.oneHot import tagoht_dic
import numpy as np

tag_vec = {}
print ("weight1 shape:" + str(weight1.shape))
# print('test:',weight1)

my = np.matrix(weight1)

# tagoht_dic为每一个key与其one hot向量组成的字典
for key in tagoht_dic.keys():
    tagoht = tagoht_dic[key]
    mx = np.matrix(tagoht)
    x = mx * my
    # print(x.shape)
    vec = np.asarray(mx * my)[0]
    tag_vec[key] = vec

#print (len(tag_vector))


