import torch
# pre-test
from transformers import *

# 加载预训练模型


pretrained_weights = 'hfl/chinese-roberta-wwm-ext-large'
# 利用模型进行预训练：分词，加CLS SEP, 补齐，截断等
tokenizer = BertTokenizer.from_pretrained(pretrained_weights)
model = BertForTokenClassification.from_pretrained(pretrained_weights)

# task-specific
input_ids = torch.tensor([tokenizer.encode("吾生也有涯，而知也无涯",add_special_tokens = True)])
with torch.no_grad():
    last_hidden_states = model(input_ids)
    print(last_hidden_states)


