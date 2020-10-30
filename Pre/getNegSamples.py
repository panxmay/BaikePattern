neglist = []
poslist = []
negset = set()
posset = set()



def geo_process():
    # 地理数据
    path = '../data/notIsA.txt'
    path_pos = '../data/isA.txt'

    for line in open(path, 'r', encoding='utf-8'):
        item = str(line.strip()).split(';;;;ll;;;;boarder;;;;ll;;;;')
        if len(item) < 2:
            continue
        neglist.append(item)
        negset.add(item[0])
        negset.add(item[1])

    for line in open(path_pos, 'r', encoding='utf-8'):
        item = str(line.strip()).split(';;;;ll;;;;boarder;;;;ll;;;;')
        if len(item) < 2:
            continue
        poslist.append([item[0],item[1][:-1]])
        posset.add(item[0])
        posset.add(item[1][:-1])

def cov_process():
    path = '../../data/negative_samples.txt'
    path_pos = '../../data/positive_samples.txt'

    for line in open(path, 'r', encoding='utf-8'):
        item = str(line.strip()).split(';;;;ll;;;;boarder;;;;ll;;;;')
        if len(item) < 2:
            continue
        neglist.append(item)
        negset.add(item[0])
        negset.add(item[1])

    for line in open(path_pos, 'r', encoding='utf-8'):
        item = str(line.strip()).split(';;;;ll;;;;boarder;;;;ll;;;;')
        if len(item) < 2:
            continue
        poslist.append([item[0],item[1]])
        posset.add(item[0])
        posset.add(item[1])
geo_process()
# cov_process()