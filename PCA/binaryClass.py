# -*- coding: utf-8 -*-

# 训练二分类模型SVM
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from BaikePattern.PCA.PCAAlgorithm import finalDf

data = finalDf[finalDf.columns[0:-1]]
cls = list(finalDf.iloc[:,-1])

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

clf = SVC(C=1.7, coef0=0.0,decision_function_shape='ovr',
          degree=3, gamma='auto', kernel='rbf')
predict = cross_val_predict(clf, data, cls, cv=10)

confusion_matrix = metrics.confusion_matrix(cls, predict)
accuracy = metrics.accuracy_score(cls, predict)
f1 = metrics.f1_score(cls, predict)
precision = metrics.precision_score(cls,predict)
recall = metrics.recall_score(cls,predict)

print (" ******************************* ")
print (" -------- SVM result ----------- ")
print ("F1: " + str(f1))
print ("accuracy: " + str(accuracy))
print ("precision: " + str(precision))
print ("recall: " + str(recall))
print (confusion_matrix)
print (" ******************************* ")

# random forest
clf = RandomForestClassifier(n_estimators=25)
predict = cross_val_predict(clf, data, cls, cv=10)

confusion_matrix = metrics.confusion_matrix(cls, predict)
accuracy = metrics.accuracy_score(cls, predict)
f1 = metrics.f1_score(cls, predict)
precision = metrics.precision_score(cls,predict)
recall = metrics.recall_score(cls,predict)

print (" ******************************* ")
print (" ----- Random forest result ------")
print ("F1: " + str(f1))
print ("accuracy: " + str(accuracy))
print ("precision: " + str(precision))
print ("recall: " + str(recall))
print (confusion_matrix)
print (" ******************************* ")

