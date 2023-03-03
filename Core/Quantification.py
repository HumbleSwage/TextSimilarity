import pandas as pd
import numpy as np


class quantification:
    """
    @todo:计算TFIDF
    @return:result[[文章1的tfidf],[文章2的tfidf]···]
    @params:term_list{词1:num1,词2:num2···}
            doc_list:文章分词后组成的list[[文章1分词结果,文章2分词结果],···]
    """

    def __init__(self):
        self.tf = pd.DataFrame()
        self.idf = pd.Series()
        self.idIdf = []

    def quantification(self, termList, docList):
        numDocs = len(docList)
        numTerms = len(termList)

        # 先计算tf
        self.tf = pd.DataFrame(
            data=np.zeros(shape=(numDocs, numTerms)), columns=termList
        )
        for idxDoc, doc in enumerate(docList):
            lenDoc = len(doc)
            if lenDoc > 0:
                for term in termList:
                    for termDoc in doc:
                        if termDoc == term:
                            self.tf.loc[idxDoc, term] += 1
                self.tf.loc[idxDoc, :] /= lenDoc
            else:
                continue
        # 再计算idf
        self.idf = pd.Series(
            data=np.zeros(shape=(numTerms,)), index=termList
        )
        for term in termList:
            for doc in docList:
                if term in doc:
                    self.idf.loc[term] += 1
        self.idf += 1
        self.idf /= numDocs
        self.idf = - np.log(self.idf)
        idfValue = []
        # 计算tf*idf
        for index in self.idf.index:
            idfValue.append(self.idf.loc[index])
        for index in self.tf.index:
            eachIdIdf = []
            j = 0
            eachTf = self.tf.loc[index].values[0:]
            for i in range(eachTf.size):
                if j < len(idfValue):
                    eachIdIdf.append(eachTf[i] * idfValue[j])  # TF—TDF=tf*tdf
                    j = j + 1
                else:
                    break
            self.idIdf.append(eachIdIdf)

        return self.tf, self.idf, self.idIdf
