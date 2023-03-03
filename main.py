import sys
from PyQt5.QtWidgets import QApplication
from Panel.MyMainForm import MyMainForm

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
