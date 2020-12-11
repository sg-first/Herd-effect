import xlrd

data = xlrd.open_workbook('SSML结果（吹风机）.xls')
table = data.sheet_by_name('SSML结果（吹风机）')

reviewID=0
id=1
r=3
star=2
date=4

allNum = 10636

def getCell(x,y):
    val=table.cell(x, y).value
    if val=='' or val=='n' or val=='N':
        return -1
    else:
        return val

def getProductStar(ri):
    for i in range(1,allNum):
        rii=getCell(i,reviewID)
        if rii==ri:
            s=float(getCell(i,star))
            return s
    return -1
