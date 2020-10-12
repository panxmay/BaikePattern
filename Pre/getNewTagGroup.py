
tg = []
tg_dict = {}
def geo_process():
    path = '../../data/isA.txt'
    save_path = '../../data/geo.txt'
    fw = open(save_path, 'w+', encoding='utf-8')
    for line in open(path, 'r', encoding='utf-8'):
        templist = line.strip().split(';;;;ll;;;;boarder;;;;ll;;;;')
        if len(templist) < 2:
            continue
        if templist[1][:-1] not in tg_dict.keys():
            tg_dict[templist[1][:-1]] = set()
        tg_dict[templist[1][:-1]].add(templist[0])

    for item in tg_dict:
        content = item + ' '
        if len(tg_dict[item]) == 0:
            continue
        for i in tg_dict[item]:
            content += i + ' '
        fw.write(content[:-1]+'\n')
    fw.close()

def cov_process():
    path = '../../data/positive_samples.txt'
    save_path = '../../data/cov.txt'
    fw = open(save_path,'w+',encoding='utf-8')
    for line in open(path, 'r', encoding='utf-8'):
        templist = line.strip().split(';;;;ll;;;;boarder;;;;ll;;;;')
        if len(templist) < 2:
            continue
        if templist[1] not in tg_dict.keys():
            tg_dict[templist[1]] = set()
        tg_dict[templist[1]].add(templist[0])

    for item in tg_dict:
        content = item + ' '
        if len(tg_dict[item]) == 0:
            continue
        for i in tg_dict[item]:
            content += i + ' '
        fw.write(content + '\n')
    fw.close()


# geo_process()
cov_process()

