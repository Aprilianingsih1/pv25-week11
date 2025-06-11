import sys
from PyQt5.QtWidgets import *

class ClipBoard(QWidget):
    def __init__(self):
        super(ClipBoard, self).__init__()
        self.initUI()
        
    def initUI(self):
        hb = QVBoxLayout()
        
        self.text1 = QTextEdit()
        hb.addWidget(self.text1)
        
        self.button1 = QPushButton("Copy")
        hb.addWidget(self.button1)
        
        self.text2 = QTextEdit()
        hb.addWidget(self.text2)
        
        self.button2 = QPushButton("Paste")
        hb.addWidget(self.button2)
        
        self.button1.clicked.connect(self.copy_text)
        self.button2.clicked.connect(self.paste_text)
        self.setLayout(hb)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Clipboard")
        self.show()

    def copy_text(self):
        clipboard.setText(self.text1.toPlainText())
        message = QMessageBox()
        message.setText(clipboard.text()+ " copied on clipboard")
        message.exec_()

    def paste_text(self):
        self.text2.setText(clipboard.text())

app = QApplication(sys.argv)
clipboard = app.clipboard()
window = ClipBoard()
window.setWindowTitle("Clipboard")
sys.exit(app.exec_())
