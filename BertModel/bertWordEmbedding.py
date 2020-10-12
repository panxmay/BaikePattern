from transformers import BertModel
from transformers import BertTokenizer
import os
import json
import numpy as np

concept_set = set()
concept_embedding_dict = {}
title = 'geo'
maxlen = 20

tokenizer = BertTokenizer.from_pretrained('hfl/chinese-roberta-wwm-ext-large')
model = BertModel.from_pretrained('hfl/chinese-roberta-wwm-ext-large')

path = '../data/' + title + '/concept'
name = 'concept.txt'
with open(os.path.join(path, name), 'r', encoding='utf-8') as f:
    for line in f:
        if line and line.strip():
            concept_set.add(line.strip('\n'))

embedding_dict = {}
all = len(concept_set)
current = 1
for concept in concept_set:
    input = tokenizer(concept, return_tensors='pt', padding=True, truncation=True, max_length=maxlen)
    outputs = model(**input)
    embedding = outputs[0]
    embedding = embedding.detach().numpy()
    embedding = np.reshape(embedding, (-1, embedding.shape[-1]))
    factor = embedding.shape[0]
    embedding = embedding.sum(axis=0) / factor
    embedding_dict[concept] = embedding
    print(all,current)
    current += 1

n_file = '../data/model/' + title + '/word_embedding.npy'
np.save(n_file, embedding_dict)

