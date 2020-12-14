import matplotlib.pyplot as plt
import numpy as np
import load
import networkx as nx

g=nx.Graph()#创建空的无向图
chui=load.loadPKL('吹风机跟风类.pkl')

def toWordStr(l):
    str=''
    for word,_ in l:
        str+=word+' '
    return str

allClassReviewNum=[]

reviewNum=0
for id,allClass in chui.items():
    # 每个allClass里有许多类，一个元素是一个类，一个类里有许多个评论，每个评论是一个三元组
    for aclass in allClass: # 一个类
        lastNode=None
        for review in aclass:
            allClassReviewNum.append(len(aclass))
            reviewNum+=len(aclass)
            reviewID,sumTFIDF,wordList=review
            print(reviewID)
            g.add_node(reviewID, name=reviewID, weight=0.5)
            if not lastNode is None:
                g.add_edge(lastNode,reviewID)
            lastNode=reviewID
        print('【OVER】')

nx.draw(g,with_labels = True, font_size =5, node_size =30, node_color='b')
plt.show()


def grade_mode(list):
    list_set = set(list)  # 取list的集合，去除重复元素
    frequency_dict = {}

    for i in list_set:  # 遍历每一个list的元素，得到该元素何其对应的个数.count(i)
        frequency_dict[i] = list.count(i)  # 创建dict; new_dict[key]=value

    grade_mode = []

    for key, value in frequency_dict.items():  # 遍历dict的key and value。key:value

        if value == max(frequency_dict.values()):
            grade_mode.append(key)

    return grade_mode

print(reviewNum)
print(len(allClassReviewNum))
zuida=max(allClassReviewNum)
print('最大值',zuida)
pingjun=np.mean(allClassReviewNum)
print('平均数',pingjun)

dayupingjun=0
for i in allClassReviewNum:
    if i>pingjun:
        dayupingjun+=i

print('大于平均',dayupingjun)
print('众数',grade_mode(allClassReviewNum))
plt.ylim(ymax=40, ymin=0)
plt.bar(range(len(allClassReviewNum)), allClassReviewNum)
plt.show()