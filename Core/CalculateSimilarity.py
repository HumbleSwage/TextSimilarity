import math


class calculateSimilarity:
    """
    @todo:calculateSimilarity_mode1模式2下计算向量余弦；calculateSimilarity_mode2模式2下计算向量余弦
    @return:任意两个之间的文件的余弦值 list
    @param:_vector_list 内容分词后的向量TF——IDF [[文件1向量],[文件2向量],[文件3向量]···]
           _vector_list2 文件内容分词后的向量TF-IDF [文件向量]
    """

    def __init__(self):
        self.result = []
        self.vector_list1 = []
        self.vector_list2 = 0

    def calculateSimilarityMode1(self, vectorList):  # 参照两向量计算余弦的公式
        for index1, i in enumerate(vectorList):
            for index2, j in enumerate(vectorList[index1 + 1:]):
                aVectorList = [i, j]
                part = list(map(lambda a: a[0] * a[1], zip(aVectorList[0], aVectorList[1])))
                if (math.sqrt(sum(list(map(lambda x: x ** 2, aVectorList[0])))) * math.sqrt(
                        sum(list(map(lambda x: x ** 2, aVectorList[1]))))) != 0:
                    self.result.append(sum(list(part)) / (
                                math.sqrt(sum(list(map(lambda x: x ** 2, aVectorList[0])))) * math.sqrt(
                            sum(list(map(lambda x: x ** 2, aVectorList[1]))))))
                else:
                    print("计算余弦时分母为0！")
                    self.result.append(math.nan)

        return self.result

    def calculateSimilarityMode2(self, vectorList1, vectorList2):  # vector_list2是文件的向量 vector_list1是文件夹的向量
        part1 = []
        aPart1 = []
        # 分子
        for item in vectorList1:
            part1_ = []
            for index1, i in enumerate(item):
                for index2, j in enumerate(vectorList2):
                    if index2 == index1:
                        part1_.append(i * j)
                    else:
                        continue
            aPart1.append(part1_)
        for i in aPart1:
            part1_1 = 0
            for j in i:
                part1_1 = part1_1 + j
            part1.append(part1_1)
        # 分母
        for index, item in enumerate(vectorList1):
            for index1, i in enumerate(item):
                vectorList1[index][index1] = i * i
        for index, i in enumerate(vectorList2):
            vectorList2[index] = i * i
        for i in vectorList1:
            vectorList1 = 0
            for j in i:
                vectorList1 = vectorList1 + j
            self.vector_list1.append(vectorList1)
        for i in vectorList2:
            self.vector_list2 = self.vector_list2 + i
        # 相除计算余弦
        result = []
        for index1, i in enumerate(part1):
            for index2, j in enumerate(self.vector_list1):
                if index1 != index2:
                    continue
                if ((math.sqrt(j)) * (math.sqrt(self.vector_list2))) != 0:
                    result.append(i / ((math.sqrt(j)) * (math.sqrt(self.vector_list2))))
                else:
                    print('计算余弦时分母为0！')
                    result.append(math.nan)

        return result
