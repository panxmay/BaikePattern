from transformers.modeling_bert import BertModel
from transformers import BertTokenizer, BertConfig
import os
import json
import numpy as np

concept_set = set()
concept_embedding_dict = {}
# title = 'coronavirus'
title = 'geo'
maxlen = 100

tokenizer = BertTokenizer.from_pretrained('hfl/chinese-roberta-wwm-ext-large')
model = BertModel.from_pretrained('hfl/chinese-roberta-wwm-ext-large')

path = '../data/' + title + '/concept'
name = 'concept.txt'
with open(os.path.join(path, name), 'r', encoding='utf-8') as f:
    for line in f:
        if line and line.strip():
            concept_set.add(line.strip('\n'))

s_path = '../data/' + title + '/concept'
s_name = 'concept_summary.json'
synonym_name = 'concept_synonyms.json'
border_name = "concept_borders.json"
s_f = open(os.path.join(s_path, s_name),'r', encoding='utf-8')
# 更新同义词库
syn_f = open(os.path.join(s_path, synonym_name),'r', encoding='utf-8')
bor_f = open(os.path.join(s_path, border_name),'r', encoding='utf-8')
concept_summary_dict = json.load(s_f)
concept_synonyms_dict = json.load(syn_f)
concept_border_dict = json.load(bor_f)
for i in concept_border_dict:
    if i in concept_synonyms_dict.keys():
        concept_border_dict[i].update(concept_synonyms_dict[i].items())

    if i in concept_summary_dict.keys():
        concept_border_dict[i].update(concept_summary_dict[i].items())



embedding_dict = {}
all = len(concept_set)
current = 1
for concept in concept_set:
    if concept in concept_border_dict.keys():
        summary_dict = concept_border_dict[concept]

        embedding_list = []
        flag = 1
        for source, summary in summary_dict.items():
            if len(summary)==0:
                continue
            flag = 0
            # 使用Bert模型进行预训练
            input = tokenizer(str(summary), return_tensors='pt', padding=True, truncation=True, max_length=maxlen)
            outputs = model(**input)
            embedding_list.append(outputs[0])
        if flag:
            continue
        # 残差链接和归一化处理
        embedding = np.zeros(shape=(1024,), dtype='float32')
        norm_factor = len(embedding_list)
        for em in embedding_list:
            e = em.detach().numpy()
            e = np.reshape(e, (-1, e.shape[-1]))
            shape_factor = e.shape[0]
            e = e.sum(axis=0) / shape_factor
            embedding += e
        if norm_factor!=0:
            embedding /= norm_factor
        embedding_dict[concept] = embedding
    print(all,current)
    current += 1

n_file = '../data/model/' + title + '/summary_embedding.npy'
np.save(n_file, embedding_dict)

