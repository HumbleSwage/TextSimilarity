from PyQt5 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 1000)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(100)
        Form.setFont(font)

        # 对应三个文件路径显示
        self.GetlineEdit1 = QtWidgets.QLineEdit(Form)
        self.GetlineEdit1.setGeometry(QtCore.QRect(150, 50, 500, 40))
        self.GetlineEdit1.setObjectName("GetlineEdit1")
        self.GetlineEdit2 = QtWidgets.QLineEdit(Form)
        self.GetlineEdit2.setGeometry(QtCore.QRect(150, 100, 500, 40))
        self.GetlineEdit2.setObjectName("GetlineEdit2")
        self.GetlineEdit3 = QtWidgets.QLineEdit(Form)
        self.GetlineEdit3.setGeometry(QtCore.QRect(150, 150, 500, 40))
        self.GetlineEdit3.setObjectName("GetlineEdit3")
        # 对应最佳相似度的显示框
        self.GetlineEdit = QtWidgets.QLineEdit(Form)
        self.GetlineEdit.setGeometry(QtCore.QRect(150, 250, 500, 40))
        self.GetlineEdit.setObjectName("GetlineEdit")
        # 对应结果显示框
        self.GetTextEdit = QtWidgets.QTextEdit(Form)
        self.GetTextEdit.setGeometry(QtCore.QRect(50, 300, 600, 490))
        self.GetTextEdit.setObjectName("GetlineEditL")
        self.GetTextEdit.setText("                                           使用手册请在使用本程序前仔细阅读\n"
                                 "                                                本程序实现文本相似度比较\n"
                                 "          选中文档再选中一个文件夹代表分析该文档与该文件夹下每一个文档的相似度\n"
                                 "          若你想要分析文件夹下任意两个文件的相似度只需点击分析文件夹再选中目标\n"
                                 "          若想分析两个文档相似度我们建议你将他们放在一个文件夹下再选中该文件夹\n"
                                 "     +++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                 "        选中目标后只需点击开始分析即可开始分析,本程序尚未得到算法优化请耐心等待\n"

                                 "     +++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
                                 "                如使用中存在任何问题请及时联系我们管理员d_zhao_work@163.com\n    "
                                 "                                                          感谢你的使用\n"
                                 )

        # 对应三个文件按钮
        self.getButton1 = QtWidgets.QPushButton(Form)
        self.getButton1.setGeometry(QtCore.QRect(50, 50, 100, 40))
        self.getButton1.setObjectName("getButton2")
        self.getButton2 = QtWidgets.QPushButton(Form)
        self.getButton2.setGeometry(QtCore.QRect(50, 100, 100, 40))
        self.getButton2.setObjectName("getButton2")
        self.getButton3 = QtWidgets.QPushButton(Form)
        self.getButton3.setGeometry(QtCore.QRect(50, 150, 100, 40))
        self.getButton3.setObjectName("getButton3")

        # 对应开始分析按钮
        self.getButtonConfirm = QtWidgets.QPushButton(Form)
        self.getButtonConfirm.setGeometry(QtCore.QRect(50, 200, 605, 50))
        self.getButtonConfirm.setObjectName("getButtonConfirm")
        # 对应最佳相似度的按钮
        self.getButtonx = QtWidgets.QPushButton(Form)
        self.getButtonx.setGeometry(QtCore.QRect(50, 250, 100, 40))
        self.getButtonx.setObjectName("getButtonx")

        # 新加功能
        self.getButtonA = QtWidgets.QPushButton(Form)
        self.getButtonA.setGeometry(QtCore.QRect(50, 800, 100, 40))
        self.getButtonA.setObjectName("getButtonA")
        self.getButtonB = QtWidgets.QPushButton(Form)
        self.getButtonB.setGeometry(QtCore.QRect(290, 800, 100, 40))
        self.getButtonB.setObjectName("getButtonB")
        self.getButtonC = QtWidgets.QPushButton(Form)
        self.getButtonC.setGeometry(QtCore.QRect(540, 800, 100, 40))
        self.getButtonC.setObjectName("getButtonC")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "文件相似度比较程序"))
        self.getButton1.setText(_translate("Form", "目标文件"))
        self.getButton2.setText(_translate("Form", "目标文件夹"))
        self.getButton3.setText(_translate("Form", "分析文件夹"))
        self.getButtonConfirm.setText(_translate("Form", "开始分析"))
        self.getButtonx.setText(_translate("Form", "最佳相似度"))
        self.getButtonA.setText(_translate("Form", "查看最佳"))
        self.getButtonB.setText(_translate("Form", "提高精读"))
        self.getButtonC.setText(_translate("Form", "查看失败"))
