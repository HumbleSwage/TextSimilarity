class beautifulOut:
    """
    @todo:本类用于美化输出结果
    @attention:请区分不同模式下文件需要传入的参数的格式
    @author:DengZhao
    """

    def __init__(self):
        self.dic_ = []
        self.dic = {}

    def beautifulOutMode1(self, list1, list2):
        for index, i in enumerate(list1):
            for j in list1[index + 1:]:
                self.dic_.append(i.split("/")[-1] + "<===>" + j.split("/")[-1])
        for index, i in enumerate(self.dic_):
            self.dic[i] = list2[index]
        self.dic = sorted(self.dic.items(), key=lambda d: d[1], reverse=True)
        return self.dic

    def beautifulOutMode2(self, list1, list2):
        for i in list2[0:-1]:
            self.dic_.append(str(list2[-1]).split("/")[-1] + "<===>" + str(i).split("/")[-1])
        for index, i in enumerate(self.dic_):
            self.dic[i] = list1[index]
        dic = sorted(self.dic.items(), key=lambda d: d[1], reverse=True)
        return dic

    def finishingLength(self, dic):
        for eachDic in dic:
            print(eachDic.key)
