# -*- coding: utf-8 -*-
from  .word  import li_one

f = open(r'C:\Users\mengyi\Desktop\result\file.txt','r')

#######################################
# 统计file中的资源个数
# content_tag: 162194
#######################################

user_tag = {}
content_tag = {}
wordInFile = []  # 存file中的所有tag
for line in f.readlines():
    linelist = line.strip().split('\t')
    tag = linelist[1]
    content = linelist[0]
    wordInFile.append(tag)
    
    ####################################
    # content 和对应的tag
    # content_tag
    if(content_tag.has_key(content)):
        content_tag[content] = content_tag[content] + '\t' + tag
    else:
        content_tag[content] = tag
    
    """
    ####################################
    ## user和其使用的tag ---> 暂时不用
    # user_tag
    if(user_tag.has_key(user)):
        user_tag[user] = user_tag[user] + '\t' + tag
    else:
        user_tag[user] = tag
    """
f.close()
print ("--------------------------------------------------")
print ("file文件中不重复的tag数目： " + str(len(list(set(wordInFile)))))
print ("resource_tag 个数：" + str(len(content_tag)))

###########################################
## 将字典 content_tag中value值由 str 转化为 list
##########################################
content_li = []   # 存content对应的tag数目，用于统计tag数目分布情况
for content in content_tag.keys():
    tags = list(set(content_tag[content].strip().split('\t')))
    content_tag[content] = tags
    content_li.append(len(content_tag[content]))
    
#print list(set(content_li))
#print len(list(set(content_li)))
######################################################
# content对应的tag个数如下：
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 18, 20, 22
######################################################
    
###################################################
#  统计tag个数对应content个数
#  num_time  --> key:tag个数, value:content个数
###################################################
"""
num_time = {}
for i in range(len(content_li)):
    num = content_li[i]
    if(num_time.has_key(num)):
        num_time[num] += 1
    else:
        num_time[num] = 1

print len(num_time)
print num_time
"""   
###########################################
#content个数以及对应出现的resource的个数
#{1: 118989, 2: 30939, 3: 8666, 4: 2586, 5: 680,
# 6: 228, 7: 68, 8: 21, 9: 6, 10: 3, 11: 3, 12: 2, 
# 18: 1, 20: 1, 22: 1}
################################################

#################################################################################
# 功能：过滤tag数目为 1 和 2 的content
# 考虑到需要找上下位词的context，是基于resource的，所以将tag数目为1和2的content删除
# 只考虑tag数目 大于3的content
# 过滤之后的数据还有 12266 条
#################################################################################
content_tag_filte = {}  # content_tag_filte 存过滤之后的content：tag
taglist = []   # 存放过滤之后的数据条目中包含的tag的个数 ， 330个词
for content in content_tag.keys():
    if(len(content_tag[content]) > 2):
        content_tag_filte[content] = content_tag[content]
        for i in range(len(content_tag_filte[content])):
            taglist.append(content_tag_filte[content][i])
#print "tag数目1和2过滤之后的content个数： " + str(len(content_tag_filte))
#print "tag数目1和2过滤之后不重复的tag个数： " + str(len(list(set(taglist)))) 
#print content_tag_filte

"""
s = open(r'C:\Users\mengyi\Desktop\result\res_tag.txt','a')
for key in content_tag_filte.keys():
    s.write(key + " : " + str(content_tag_filte[key]) + '\n')
s.close()
"""

################################################################
# 统计那些词不在过滤之后的文件中 list(set(taglist)) 
# 应该含有的tag （li_one）
#################################################################
"""
notinTag = []
print "原始tag总数： " + str(len(li_one))
print "过滤后file文件含有tag数目: " + str(len(list(set(taglist))))

for i in range(len(li_one)):
    if(li_one[i].lower() not in list(set(taglist))):
        notinTag.append(li_one[i])
    
print "文件中未包含的tag有 %d " % len(notinTag)

li_one.sort()
#print li_one

notinTag.sort()
print notinTag

"""
##################################################################
## 从原始file文件中删除tag数目为 1 和 2 的content
# content_tag_filte的key为content，
# 直接和原始file进行匹配，content_tag_filte中不存在的content不进行存储
#################################################################
"""
f = open(r'C:\Users\mengyi\Desktop\result\file.txt','r')
s = open(r'C:\Users\mengyi\Desktop\result\file_filter.txt','a')

# content
content = content_tag_filte.keys()
sum = 0
for line in f.readlines():
    contentInLine = line.strip().split('\t')[2]
    if(contentInLine in content):
        s.write(line)
        sum += 1
f.close()
s.close()
print "过滤之后的数据有 %d 条" % sum
"""   











 
    



"""
print content_tag      
print "user_tag: " + str(len(user_tag))
print "content_tag: " + str(len(content_tag))
"""