import load
import load2
import nltk.tokenize as tk
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

allReviewText=[]
allOtherInfo=[]

tokenizer = tk.WordPunctTokenizer()

if __name__=='__main__':
    for i in range(1, load.allNum):
        reviewID = load.getCellT1(i, load.reviewID)
        star=load2.getProductStar(reviewID)
        if star==-1:
            continue
        print(reviewID)
        allReviewText.append(load.getReviewText(i))
        date=load.getDate(i)
        id=load.getCellT1(i, load.id)
        allOtherInfo.append((id,date,reviewID,star))

    load.savePKL('微波炉info.pkl', allOtherInfo)

    print('finish')

    vectorizer=CountVectorizer() # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer=TfidfTransformer() # 该类会统计每个词语的tf-idf权值
    tfidf=transformer.fit_transform(vectorizer.fit_transform(allReviewText)) # 第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word=vectorizer.get_feature_names() # 获取词袋模型中的所有词语
    weight=tfidf.toarray()

    allTFIDF=[]

    for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
        l=[]
        for j in range(len(word)):
            if weight[i][j]!=0:
                l.append((word[j],weight[i][j]))
        allTFIDF.append(l)

    load.savePKL('微波炉tfidf.pkl', allTFIDF)

    print('finish')