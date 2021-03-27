from sklearn.feature_extraction.text import CountVectorizer

def findSpam(traindata,testdata):
    cv=CountVectorizer()
    X=cv.fit(traindata).toarray()
    Y=cv.transform(testdata)
    return y