from BaikePattern.Pre.getNegSamples import poslist
import json
import random

title = 'coronavirus'

path_positive = '../data/'

summary_file = 'concept_summary.json'

concept_file = "concept.txt"


def create_sample(file, ori_list, bIspositive):
    res = []

    with open(file, encoding="utf-8") as f:
        load_dict = json.load(f)

        for elem in ori_list:
            if elem[0] not in load_dict.keys() or elem[1] not in load_dict.keys():
                continue

            default = '-1'

            baidu = default

            if "baidu" in load_dict[elem[0]].keys():
                baidu = load_dict[elem[0]]['baidu']

            toutiao = default

            if "toutiao" in load_dict[elem[0]].keys():
                toutiao = load_dict[elem[0]]['toutiao']

            zhwiki = default

            if "zhwiki" in load_dict[elem[0]].keys():
                zhwiki = load_dict[elem[0]]['zhwiki']

            res_one = baidu + ";;;" + toutiao + ";;;" + zhwiki

            baidu = default

            if "baidu" in load_dict[elem[1]].keys():
                baidu = load_dict[elem[1]]['baidu']

            toutiao = default

            if "toutiao" in load_dict[elem[1]].keys():
                toutiao = load_dict[elem[1]]['toutiao']

            zhwiki = default

            if "zhwiki" in load_dict[elem[1]].keys():
                zhwiki = load_dict[elem[1]]['zhwiki']

            res_two = baidu + ";;;" + toutiao + ";;;" + zhwiki

            res.append([res_one, res_two, bIspositive])

    return res


def create_negative(file, concept, positive, count):
    ori_list = []

    ori_keys = []

    for line in open(concept):
        ori_keys.append(line.strip())

    while count:
        one = random.randint(0, len(ori_keys) - 1)

        two = random.randint(0, len(ori_keys) - 1)

        key = [ori_keys[one], ori_keys[two]]

        if key not in positive and key not in ori_list:
            count = count - 1

            ori_list.append(key)

    return create_sample(file, ori_list, 0)


baidu = "baidu"

toutiao = "toutiao"

zhwiki = "zhwiki"

sources = [baidu, toutiao, zhwiki]


def create_key_sample(file, ori_list, keys, bIspositive):
    res = []

    with open(file, encoding="utf-8") as f:
        load_dict = json.load(f)

        for elem in ori_list:
            if elem[0] not in load_dict.keys() or elem[1] not in load_dict.keys():
                continue

            default = '-1'

            res_one = default

            if keys[0] in load_dict[elem[0]].keys():
                res_one = load_dict[elem[0]][keys[0]]

            res_two = default

            if keys[1] in load_dict[elem[0]].keys():
                res_two = load_dict[elem[0]][keys[1]]

            res.append([res_one, res_two, bIspositive])

    return res


def create_key_negative(file, concept, positive, count, keys):
    ori_list = []

    ori_keys = []

    for line in open(concept):
        ori_keys.append(line.strip())

    while count:
        one = random.randint(0, len(ori_keys) - 1)

        two = random.randint(0, len(ori_keys) - 1)

        key = [ori_keys[one], ori_keys[two]]

        if key not in positive and key not in ori_list:
            count = count - 1

            ori_list.append(key)

    return create_key_sample(file, ori_list, keys, 0)


positive_dict = {}

for i in sources:
    for j in sources:
        key = i + "_" + j

        positive_dict[key] = create_key_sample(path_positive + title + '/concept/' + summary_file, poslist, [i, j], 0)

negative_dict = {}

for i in sources:
    for j in sources:
        key = i + "_" + j

        negative_dict[key] = create_key_negative(path_positive + title + '/concept/' + summary_file,
                                                 path_positive + title + '/concept/' + concept_file, poslist, 1000,
                                                 [i, j])
