from Reader.ReadFileContent import readFileContent
import os


class readContentAndPath:
    """
    @todo:将指定文件夹处理成要求格式;将指定文件处理成要求格式
    @return:doc_list为文档的内容["文件1的内容","文件2的内容",···]
            path_list为文档的地址["文件1的地址","文件2的地址"···]
    @param:_dir指定文件夹的绝对路径;_file指定文件的绝对路径
    """

    def __init__(self):
        self.doc_list = []  # 内容
        self.path_list = []  # 成功的地址
        self.path_list_fail = {}  # 失败的地址
        self.i = 1  # 文件统计个数
        self.msg = 0  # 错误信息的报错

    def readDocument(self, _dir):
        list = os.listdir(_dir)  # 获取文件夹下文件
        for i in range(0, len(list)):  # 循环对单个文件进行操作
            path = os.path.join(_dir, list[i])  # 拿到单个文件，即path就是一个文件路径
            if os.path.isdir(path):  # 判断文件夹
                self.readDocument(path)  # 嵌套调用
            if os.path.isfile(path) & ((".txt" in path) | (".docx" in path) | (".pdf" in path)):  # 判断文件
                self.readFile(path)  # 读取内容
        return

    def readFile(self, _file):
        print(str(self.i) + _file)
        readFileContent_ = readFileContent()  # 生成对象
        if ".txt" in _file:  # 处理txt文件
            content, msg = readFileContent_.readTxt(_file)
            if msg == 1:
                self.path_list.append(_file)  # 地址添加到path_list
                self.doc_list.append(content)  # 内容添加到doc_list
            else:
                print("---------")
        elif ".docx" in _file:  # 处理docx文件
            content, msg = readFileContent_.readWord(_file)
            print(msg)
            if msg == 1:
                self.path_list.append(_file)  # 地址添加到path_list
                self.doc_list.append(content)  # 内容添加到doc_list
            else:
                print("++++++++++")
        elif ".pdf" in _file:  # 处理pdf文件
            content, msg = readFileContent_.readPdf(_file)
            if msg == 1:
                self.path_list.append(_file)  # 地址添加到path_list
                self.doc_list.append(content)  # 内容添加到doc_list
            else:
                print("===========")
        else:  # 不满要要求的格式
            self.msg = 2
            print(_file + "不满足格式要求！")
        self.i = self.i + 1
        return
