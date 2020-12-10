import xlrd
import pickle

data = xlrd.open_workbook('microwave.xlsx')
table = data.sheet_by_name('microwave')

reliability = 0
help = 9
total = 10
date = 15
title = 6
review1 = 13
review2 = 14
id = 4
reviewID = 3
star = 8

allNum = 1557

def getCellT1(x,y):
    val=table.cell(x, y).value
    return val

def getDateList(x):
    d = table.cell(x, date).value
    return d.split('/')

def getDate(x):
    d=getDateList(x)
    if len(d)!=3:
        return -1
    else:
        fd=float(d[2])-2000+float(d[0])/12-float(d[1])/365
        return fd

def getReviewText(i):
    r1=getCellT1(i,review1)
    r2=getCellT1(i,review2)
    if not isinstance(r1,str):
        r1=''
    if not isinstance(r2,str):
        r2=''
    return r1+' '+r2

def writeFile(filePath, content):
    print('Write info to file:Start...')
    # 将文件内容写到文件中
    with open(filePath, 'a', encoding='utf-8') as f:
        f.write(content)
        print('Write info to file:end...')

def readFile(filepath):
    f=open(filepath,'r')
    return f.read()

def savePKL(filePath,data):
    f = open(filePath, 'wb')
    pickle.dump(data, f)
    f.close()

def loadPKL(filePath):
    f = open(filePath, 'rb')
    chui = pickle.load(f)
    f.close()
    return chui