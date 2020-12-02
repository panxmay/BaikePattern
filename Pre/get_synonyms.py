import synonyms
import json
import codecs

title = 'geo'

path = '../data/geo/concept/concept.txt'
path_km = '../data/'+title+'/from_km.json'
km_dict = json.load(open(path_km,'r',encoding='utf-8'))
syn_dict = {}
for line in open(path,'r',encoding='utf-8'):
    syn_dict[line.strip()] = {'synonyms':[],'Mag':[],'km':[]}
    syn_dict[line.strip()]['synonyms'] = synonyms.nearby(line.strip())[0]
    syn_dict[line.strip()]['km'] = km_dict[line.strip()]['synonyms']

s_path = '../data/'+title+'/concept/concept_synonyms.json'
fp = codecs.open(s_path,'w+',encoding='utf-8')
fp.write(json.dumps(syn_dict, ensure_ascii=False, indent=4, separators=(',', ':')))
fp.close()


