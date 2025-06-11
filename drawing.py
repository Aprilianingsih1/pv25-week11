import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Drawing(QWidget):

    def __init__(self):
        super(Drawing, self).__init__()
        self.setGeometry(300,300,850,500)
        self.setWindowTitle("Drawing")

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setPen(QColor(Qt.black))
        qp.setFont(QFont('comic', 20))
        qp.drawText(10, 30, "Drawing")

        qp.setPen(QColor(Qt.red))
        qp.drawLine(10, 50, 230, 50)

        qp.setPen(QColor(Qt.blue))
        qp.drawLine(10, 60, 230, 60)

        qp.setPen(QColor(Qt.blue))
        qp.drawEllipse(350,25,100,100)

        qp.setPen(QColor(Qt.darkCyan))
        qp.drawEllipse(400, 25, 100, 100)

        qp.setPen(QColor(Qt.red))
        qp.drawEllipse(375, 25, 100, 100)

        qp.drawPixmap(350, 0, QPixmap("toga.jpg"))

        qp.setPen(QColor(Qt.red))
        qp.fillRect(10,75,100,100, QBrush(Qt.Dense1Pattern))
        qp.drawRect(150, 75, 100, 100)

        qp.drawRect(10, 200, 100, 100)
        qp.fillRect(150, 200, 100, 100, QBrush(Qt.Dense1Pattern))
        qp.end()

def main():
   app = QApplication(sys.argv)
   drawing = Drawing()
   drawing.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
