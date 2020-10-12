# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense, Activation, Input
from folksonomy.exp.main.OurModel.trainData import train
from keras import backend as K
import numpy as np
import tensorflow as tf
from folksonomy.exp.main.OurModel.oneHot import taglist
from keras import layers
from keras import metrics
from keras import regularizers
from keras import optimizers
from keras import losses

epochs = 10

# train 第一列是输入向量，第二列是上位词的one-hot向量
x_train = []
y_train = []

# n = 451
# 头条和百度百科数据
# n = 3331
# 地理数据
# n = 535
# 新冠数据
# n = 425
n = len(taglist)
for i in range(len(train)):
    x_train.append(train[i][0])
    y_train.append(train[i][1])
x_train = np.array(x_train)
y_train = np.array(y_train)


print ("x_train shape: " + str(x_train.shape))
print ("y_train shape: " + str(y_train.shape))

# ------------------------------
model = Sequential()
#dense层是全连接层，activity_regularizer是正则化项，units为输出矩阵的第二个维度数量
layer1 = Dense(units=50, activation='relu', use_bias=True, kernel_initializer='random_uniform',
                bias_initializer='zeros',input_shape=(n,),
                activity_regularizer=regularizers.l1(0.01))
model.add(layer1)


layer2 = Dense(units=n,activation='softmax', use_bias=True, kernel_initializer='random_uniform',
                bias_initializer='zeros',
                activity_regularizer=regularizers.l1(0.01))
model.add(layer2)

# loss: cross_entropy
# true为真实值，pred为预测值
def my_loss(y_true,y_pred):
    # 压缩矩阵求和
    # 压缩第二个维度，结果为 1 X 第一个维度的长度
    # y_true是一个1 X 3331的列向量
    l1 = -tf.reduce_sum(tf.multiply(y_true,K.log(y_pred)),axis=1)
    # loss =K.sum(l1,axis=0)
    return l1

def top_k_accu(y_true,y_pred):
    y_true = y_true[:,:-1]
    return metrics.top_k_categorical_accuracy(y_true,y_pred,k=1)


"""
lr：一个Tensor浮点值，或者是的时间表 tf.keras.optimizers.schedules.LearningRateSchedule，或者是不带任何参数并返回要使用的实际值的可调用对象。学习率。防御到0.001。
rho：历史/即将到来的梯度的折现因子。默认为0.9。
epsilon：数值稳定性的一个小常数。默认为1e-7。
"""
rmsProp = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-06)
model.compile(optimizer=rmsProp, loss=my_loss, metrics=['accuracy'])

#model.summary()
model.fit(x_train, y_train, validation_split=0.2, epochs=epochs
          , batch_size=32)


layer1_weights = layer1.get_weights()   
layer2_weights = layer2.get_weights()

# 得到权重矩阵
weight1 = layer1_weights[0]
weight2 = layer2_weights[0]

if __name__ == '__main__':
    print('model')
