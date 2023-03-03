import jieba_fast


class cutSelectContent:
    """
    @todo:实现对文章的分词和词的统计
    @return:term_list:词的个数{词1:num1,词2:num2···}
            doc_list:文章分词后组成的list[[文章1分词结果,文章2分词结果],···]
    @param:doc_list:文章内容[文章1内容,文章2内容····]
    """

    def __init__(self):
        self.term_list = {}  # 统计词、词频
        self.doc_list = []  # 内容分词结果
        self.terms = []  # 分词后单篇文章的结果
        self.term = []  # 去除停用词后单篇文章的结果
        self.stopWordList = []  # 停用词

    def segmentation(self, _docList):
        try:
            with open('Source/stopwords.txt', mode='r', encoding='utf-8') as stopWord:  # 读取文件
                for i in stopWord.readlines():  # 选择以每一行读取
                    self.stopWordList.append(i.strip())  # 将以每一行除去后面的空格
            self.stopWordList.append(" ")  # 将停用词保存在一个list中
        except FileNotFoundError as e:  # 报错信息
            print(e)
        except IOError as e:
            print(e)
        finally:  # 防止程序异常退出
            if len(self.stopWordList) <= 0:
                self.stopWordList = [";", "。", " ", "/", "?", "!", ".", ","]  # 临时添加该停用词列表，将报错信息返回
        for i, j in enumerate(_docList):  # 内容
            self.term = []
            self.terms = []
            try:
                self.terms = list(jieba_fast.cut(j))  # 对内容进行切分并转换为list
            except NameError as e:
                print(e)
            finally:
                if len(self.terms) <= 0:
                    self.terms = ["00", "00", "00", "00"]  # 发生错误，防止程序中断进行填补
            for m in self.terms:
                if m not in self.stopWordList:
                    self.term.append(m)
                else:
                    continue
            self.doc_list.append(self.term)  # 将分词结果放入doc_list
            for term in self.term:  # 循环terms
                if self.term_list.get(term):  # 判断term_list中是否已经存在term
                    self.term_list[term] += 1  # 存在则加1
                else:
                    self.term_list[term] = 1  # 不存在则令其value为1
        return self.term_list, self.doc_list
