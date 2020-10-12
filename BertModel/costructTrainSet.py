import numpy as np
import os
# from utils.process_utils import get_triple
import opencc



cc = opencc.OpenCC('t2s')
title = 'geo'
path ='../data/model/' + title
word_file = 'word_embedding.npy'
summary_file = '/summary_embedding.npy'
summary_dict = np.load(path + summary_file, allow_pickle=True).item()

feature_list = []
label_list = []

with open(os.path.join(path, 'positive_samples.txt'), 'r', encoding='utf-8') as f:
    for line in f:
        if line and line.strip():

            s, p, o = get_triple(line)
            s_array = summary_dict.get(cc.convert(s), [])
            o_array =summary_dict.get(cc.convert(o), [])
            if len(s_array)>0 and len(o_array)>0:
              # s and o
              new_array = np.concatenate((s_array, o_array))
              # s - o
              new_array = np.concatenate((new_array, s_array-o_array))
              # s * o
              new_array = np.concatenate((new_array, [np.dot(s_array, o_array)]))
              feature_list.append(new_array)
              label_list.append(1)

with open(os.path.join(path, 'negative_samples.txt'), 'r', encoding='utf-8') as f:
    for line in f:
        if line and line.strip():
            # s, p, o = get_triple(line)
            s_array = summary_dict.get(cc.convert(s), [])
            o_array = summary_dict.get(cc.convert(o), [])
            if len(s_array) > 0 and len(o_array) > 0:
                # s and o
                new_array = np.concatenate((s_array, o_array))
                # s - o
                new_array = np.concatenate((new_array, s_array - o_array))
                # s * o
                new_array = np.concatenate((new_array, [np.dot(s_array, o_array)]))
                feature_list.append(new_array)
                label_list.append(0)

np.save(path + '/features.npy', feature_list)
np.save(path + '/label.npy', label_list)
