# -*- coding: utf-8 -*-

# 训练二分类模型SVM
from sklearn.svm import SVC
from BaikePattern.MacBertModel.binaryClass_train import train_vec
import numpy as np
import random
from sklearn import metrics
import joblib

from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import cross_val_score
import scipy.spatial.distance as distance
from sklearn.ensemble import RandomForestClassifier

title = 'geo'
# title = 'coronavirus'
test = -60

data = []  # data为两个tag vector的拼接
cls = []   # class

random.shuffle(train_vec)

for i in range(len(train_vec)):
    item = train_vec[i]
    tag1_vec = list(item[0])
    tag2_vec = list(item[1])
    offset = np.array(tag1_vec) - np.array(tag2_vec)
    sim = []
    cosSim = 1 - distance.cosine(tag1_vec, tag2_vec)
    sim.append(cosSim)
    tag1_vec.extend(tag2_vec)
    tag1_vec.extend(list(offset))
    tag1_vec.extend(sim)

    cls_item = item[2]
    data.append(np.array(tag1_vec))
    cls.append(cls_item)
print ("len of data: " + str(len(data[0])))


# svm
"""
C 浮点数，默认= 1.0.正则化参数。正则化的强度与C成反比。必须严格为正。惩罚是平方的l2惩罚。
内核{'linear'，'poly'，'rbf'，'sigmoid'，'precomputed'}，默认='rbf'
指定算法中要使用的内核类型。它必须是“线性”，“多边形”，“ rbf”，“ Sigmoid”，“预先计算”或可调用的一个。如果没有给出，将使用“ rbf”。如果给出了可调用对象，则将其用于根据数据矩阵预先计算内核矩阵；那个矩阵应该是一个形状的数组。(n_samples, n_samples)

度int，默认= 3
多项式内核函数的度（“ poly”）。被所有其他内核忽略。
如果gamma='scale'（默认）被传递，则它将1 /（n_features * X.var（））用作gamma值，
如果为'auto'，则使用1 / n_features。
"""

filename = '../data/model/'+title+'/randomForestModel.model'
clf = RandomForestClassifier(n_estimators=25)
clf.fit(data[:test],cls[:test])
# clf.fit(data,cls)
joblib.dump(clf,filename)

# 下载本地模型
model1 = joblib.load(filename)

#对本地模型进行预测
list1 = model1.predict(data)[test:]
list2 = cls[test:]

count=0
for i,j in zip(list1,list2):
   if i==j:
       count+=1

print(count/(test*-1))
# print(model1.predict(data)[test:])
# print(cls[test:])




