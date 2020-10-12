from transformers import BertModel, BertTokenizer, BertConfig
import os
import json
import numpy as np

concept_set = set()
concept_embedding_dict = {}
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
s_f = open(os.path.join(s_path, s_name),'r', encoding='utf-8')
concept_summary_dict = json.load(s_f)
embedding_dict = {}
all = len(concept_set)
current = 1
for concept in concept_set:
    summary_dict = concept_summary_dict[concept]
    if summary_dict:
        embedding_list = []
        for source, summary in summary_dict.items():
            input = tokenizer(summary, return_tensors='pt', padding=True, truncation=True, max_length=maxlen)
            outputs = model(**input)
            embedding_list.append(outputs[0])
        embedding = np.zeros(shape=(1024,), dtype='float32')
        norm_factor = len(embedding_list)
        for em in embedding_list:
            e = em.detach().numpy()
            e = np.reshape(e, (-1, e.shape[-1]))
            shape_factor = e.shape[0]
            e = e.sum(axis=0) / shape_factor
            embedding += e
        embedding /= norm_factor
        embedding_dict[concept] = embedding
    print(all,current)
    current += 1

n_file = '../data/model/' + title + '/summary_embedding.npy'
np.save(n_file, embedding_dict)

