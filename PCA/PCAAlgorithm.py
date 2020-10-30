import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from BaikePattern.Pre.getNegSamples import neglist,poslist


title = 'geo'
path = '../data/model/'+title
summary_name = '/summary_embedding.npy'
summary_dict = np.load(path+summary_name,allow_pickle=True).item()

# 获取PCAEmbedding
# 下位词+上位词+相似度
df = pd.DataFrame()
for item in poslist:
    if item[0] in summary_dict.keys() and item[1] in summary_dict.keys():
        arr = np.hstack((summary_dict[item[0]],summary_dict[item[1]]))
        # -1代表自动计算行数或列数
        vec1 = summary_dict[item[0]].reshape(1, -1)
        vec2 = summary_dict[item[1]].reshape(1, -1)
        arr = np.append(arr, cosine_similarity(vec1,vec2))
        # arr(cosine_similarity(vec1,vec2))
        arr = np.append(arr, '1').reshape(1,-1)
        df = df.append(pd.DataFrame(arr),ignore_index=True)

for item in neglist:
    if item[0] in summary_dict.keys() and item[1] in summary_dict.keys():
        arr = np.hstack((summary_dict[item[0]],summary_dict[item[1]]))
        # -1代表自动计算行数或列数
        vec1 = summary_dict[item[0]].reshape(1, -1)
        vec2 = summary_dict[item[1]].reshape(1, -1)
        arr = np.append(arr, cosine_similarity(vec1,vec2))
        # arr(cosine_similarity(vec1,vec2))
        arr = np.append(arr, '0').reshape(1,-1)
        df = df.append(pd.DataFrame(arr),ignore_index=True)

x = df.loc[:,:2048]
y = df.loc[:,2049]
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=50)
principalComponents = pca.fit_transform(x, y)
principalDf = pd.DataFrame(data = principalComponents)
# principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
finalDf = pd.concat([principalDf, y], axis = 1)



fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)
#
# targets = ['1','0']
# colors = ['r', 'g']
# for target, color in zip(targets,colors):
#     indicesToKeep = y == target
#     ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'], finalDf.loc[indicesToKeep, 'principal component 2'], c = color, s = 50)
#     ax.legend(targets)
# ax.grid()
# plt.show()
#






