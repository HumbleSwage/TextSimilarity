import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from Core.CalculateSimilarity import calculateSimilarity
from Core.Quantification import quantification
from Panel.Ui import Ui
from Processer.CutSelectContent import cutSelectContent
from Reader.ReadContentAndPath import readContentAndPath
from Utils.BeautifulOut import beautifulOut


class MyMainForm(QMainWindow, Ui):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.getButton1.clicked.connect(self.btnChooseFile)
        self.getButton2.clicked.connect(self.btnChooseDir_button2)
        self.getButton3.clicked.connect(self.btnChooseDir_button3)
        self.getButtonConfirm.clicked.connect(self.startAnalysis)
        self.getButtonA.clicked.connect(self.btnChooseDir_button)
        self.getButtonB.clicked.connect(self.btnChooseDir_button)
        self.getButtonC.clicked.connect(self.btnChooseDir_button)
        self.doc_list = []
        self.path_list = []
        self.path_list_fail = []
        self.doc_list_doc = []
        self.path_doc = []
        self.doc_list_file = []
        self.path_file = []
        self.path = []
        self.term_list = []
        self.tf = []
        self.idf = []
        self.idIdf = []
        self.similarity = []
        self.flag = True
        self.msg = ""
        self.mode = 0

    def btnChooseFile(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self,
                                                                "选取文件",
                                                                self.cwd,  # 起始路径
                                                                "*.txt *.pdf *.docx *.text")  # 设置文件扩展名过滤,用双分号间隔
        if fileName_choose == "":
            return
        self.GetlineEdit1.setText(fileName_choose)
        return fileName_choose

    def btnChooseDir_button2(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.cwd)  # 起始路径
        if dir_choose == "":
            return
        self.GetlineEdit2.setText(dir_choose)
        return dir_choose

    def btnChooseDir_button3(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      self.cwd)  # 起始路径
        if dir_choose == "":
            return
        self.GetlineEdit3.setText(dir_choose)
        return dir_choose

    def btnChooseDir_button(self):
        self.GetTextEdit.setText("")
        self.GetTextEdit.setText("功能即将开放！疑问请联系管理员d_zhao_work@163.com")

    def startAnalysis(self):
        quantify = quantification()
        # 判断框的选择情况
        if (self.GetlineEdit1.displayText() == "") & (self.GetlineEdit2.displayText() == "") & (
                self.GetlineEdit3.displayText() == ""):
            # 文件和文件夹都未选择
            self.flag = False
            self.msg = "至少需要两个目标！"
        elif (self.GetlineEdit3.displayText()) != "":  # 只选择文件夹，即分析该文件夹下面的任意两两文件的相似度
            # 获取doc_list path_list path_list_fail
            readContentAndPath_ = readContentAndPath()
            readContentAndPath_.readDocument(self.GetlineEdit3.displayText())
            self.doc_list = readContentAndPath_.doc_list
            self.path_list = readContentAndPath_.path_list
            self.path_list_fail = readContentAndPath_.path_list_fail
            # 获取tf  idf  idIdf
            cutSelectContent_ = cutSelectContent()
            self.term_list, self.doc_list = cutSelectContent_.segmentation(self.doc_list)
            print(self.term_list)
            print(len(self.doc_list))
            self.tf, self.idf, self.idIdf = quantify.quantification(self.term_list, self.doc_list)
            # 获取similarity
            calculateSimilarity_ = calculateSimilarity()
            self.similarity = calculateSimilarity_.calculateSimilarityMode1(self.idIdf)
            # 获取dic
            beautifulOut_ = beautifulOut()
            self.dic = beautifulOut_.beautifulOutMode1(self.path_list, self.similarity)
            self.flag = True
            self.mode = 1
        elif (self.GetlineEdit1.displayText() != "") & (self.GetlineEdit2.displayText() == ""):
            self.flag = False
            self.msg = "单个文件无法比较，请重新尝试！"
        elif (self.GetlineEdit1.displayText() != "") & (self.GetlineEdit2.displayText() != ""):
            # 获取doc_list path_list path_list_fail
            readContentAndPath_ = readContentAndPath()
            readContentAndPath_.readDocument(self.GetlineEdit2.displayText())
            self.doc_list = readContentAndPath_.doc_list
            readContentAndPath_.readFile(self.GetlineEdit1.displayText())
            self.doc_list = readContentAndPath_.doc_list
            print(self.doc_list)
            self.path_list = readContentAndPath_.path_list
            self.path_list_fail = readContentAndPath_.path_list_fail
            # 获取tf  idf  idIdf
            cutSelectContent_ = cutSelectContent()
            self.term_list, self.doc_list = cutSelectContent_.segmentation(self.doc_list)
            self.tf, self.idf, self.idIdf = quantify.quantification(self.term_list, self.doc_list)
            # 获取similarity
            calculateSimilarity_ = calculateSimilarity()
            self.similarity = calculateSimilarity_.calculateSimilarityMode2(self.idIdf[0:-1], self.idIdf[-1])
            # 获取dic
            beautifulOut_ = beautifulOut()
            self.dic = beautifulOut_.beautifulOutMode2(self.similarity, self.path_list)
            self.flag = True
            self.mode = 2
        elif (self.GetlineEdit1.displayText() != "") & (self.GetlineEdit2.displayText() != "") & (
                self.GetlineEdit3.displayText() != ""):
            self.flag = False
            self.msg = "无法明确你的动作！"
        else:
            self.flag = False
            self.msg = "发生未知错误！"

        if self.flag:
            if self.mode == 1:
                self.GetTextEdit.setText("")
                for index, item in enumerate(self.dic):
                    self.GetTextEdit.append(str(item))
                self.GetlineEdit.setText(str(self.dic[0][1] * 100) + "%")
            elif self.mode == 2:
                self.GetTextEdit.setText("")
                for item in self.dic:
                    self.GetTextEdit.append(str(item))
                self.GetlineEdit.setText(str(max(self.similarity) * 100) + "%")
            else:
                print("发生未知错误！")
        else:
            self.GetTextEdit.append(self.msg)
