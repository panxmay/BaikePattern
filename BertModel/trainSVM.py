from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

geo_features = np.load('../data/model/geo/features.npy',allow_pickle=True)
geo_label = np.load('../data/model/geo/label.npy',allow_pickle=True)
coronavirus_features = np.load('../data/model/coronavirus/features.npy',allow_pickle=True)
coronavirus_label = np.load('../data/model/coronavirus/label.npy',allow_pickle=True)
features = np.concatenate((coronavirus_features, geo_features), axis=0)
label = np.concatenate((coronavirus_label, geo_label), axis=0)
X_train, X_test, Y_train, Y_test = train_test_split(features, label, test_size=0.2, random_state=len(label))

thresholds = np.linspace(0.5, 0.9, 9)
Cs = np.linspace(0.1, 1, 10)

# threshold for index, threshold in enumerate(thresholds):
# c
threshold = 0.6
index = 0
recall = []
precision = []
f1 = []

for C in Cs:
    model = SVC(kernel='linear', C=1, gamma='auto',probability=True)
    model.fit(X_train, Y_train)

    pro_list = model.predict_proba(X_test)

    tp = 0
    fn = 0
    fp = 0
    tn = 0
    for i in range(len(Y_test)):
        pro_1 = pro_list[i][1]
        if pro_1 > threshold:
            if Y_test[i] == 1:
                tp = tp + 1
            else:
                fp = fp + 1
        else:
            if Y_test[i] == 0:
                tn = tn + 1
            else:
                fn = fn + 1
    precision.append(tp / (tp + fp))
    recall.append(tp / (tp + fn))
    f1.append(2 * precision[index] * recall[index] / (precision[index] + recall[index]))
    print('C: ', C, 'precision: ', precision[index], 'recall: ', recall[index], 'F1', f1[index])
    index = index+1
plt.plot(Cs, precision, label='precision')
plt.plot(Cs, recall, label='recall')
plt.plot(Cs, f1, label='F1')
plt.xlabel('C')
plt.ylabel('evaluation')
plt.legend()
plt.show()


# # threshold for index, threshold in enumerate(thresholds):
# # c
# threshold = 0.6
# index = 0
# for C in Cs:
#     model = SVC(kernel='linear', C=1, gamma='auto',probability=True)
#     model.fit(X_train, Y_train)
#
#     pro_list = model.predict_proba(X_test)
#     recall = []
#     precision = []
#     f1 = []
#
#     tp = 0
#     fn = 0
#     fp = 0
#     tn = 0
#     for i in range(len(Y_test)):
#         pro_1 = pro_list[i][1]
#         if pro_1 > threshold:
#             if Y_test[i] == 1:
#                 tp = tp + 1
#             else:
#                 fp = fp + 1
#         else:
#             if Y_test[i] == 0:
#                 tn = tn + 1
#             else:
#                 fn = fn + 1
#     precision.append(tp / (tp + fp))
#     recall.append(tp / (tp + fn))
#     f1.append(2 * precision[index] * recall[index] / (precision[index] + recall[index]))
#     print('threshold: ', threshold, 'precision: ', precision[index], 'recall: ', recall[index], 'F1', f1[index])
#     index = index+1
# plt.plot(thresholds, precision, label='precision')
# plt.plot(thresholds, recall, label='recall')
# plt.plot(thresholds, f1, label='F1')
# plt.xlabel('C')
# plt.ylabel('score')
# plt.legend()
# plt.show()