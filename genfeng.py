import pickle
import load

f = open('奶嘴tfidf.pkl', 'rb')
allText=pickle.load(f)
f = open('奶嘴info.pkl', 'rb')
allInfo=pickle.load(f)

sortList=[]
sub=0
for id,date,_ in allInfo:
    sortList.append((sub,date))
    sub+=1

sortList.sort(key=lambda r:r[1]) # 按日期排序

def countRepeat(l1:tuple,l2:tuple):
    count=[]
    for i in l1:
        for j in l2:
            if i[0]==j[0]:
                count.append(i) # l1是被检测那个list
                break
    return count

allFollow={}

for sub,date in sortList:
    text=allText[sub]
    id,_,reviewID=allInfo[sub]
    for i in range(sub): # 向前找重合的
        idJ, dateJ, reviewIDJ = allInfo[i]
        if idJ==id:
            textJ = allText[i]
            repeat = countRepeat(text,textJ)
            sumti=0
            for _,ti in repeat:
                sumti+=ti

            if sumti>3 and len(repeat)>=3:
                print(text)
                def appendNewClass():
                    newClass = []
                    newClass.append((reviewID, date, text))
                    newClass.append((reviewIDJ, dateJ, textJ))
                    allFollow[id].append(newClass)

                if not id in allFollow.keys(): # 如果商品不存在，创建商品
                    allFollow[id]=[]
                    appendNewClass()
                else:
                    isFound = False
                    for Class in allFollow[id]:
                        for reviewIDA,_,_ in Class:
                            if reviewIDA==reviewIDJ: # 从前面找到那个跟风评论已经有一类了
                                print('add')
                                Class.append((reviewID,date,text))
                                isFound=True
                                break
                        if isFound:
                            break
                    if not isFound:
                        appendNewClass()
                break # 以上几种情况都会append，所以直接匹配下一个评论即可

print(len(allFollow.items()))
load.savePKL('奶嘴跟风类.pkl', allFollow)