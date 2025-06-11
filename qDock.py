import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DockWidget(QMainWindow):
    def __init__(self, parent=None):
        super(DockWidget, self).__init__(parent)

        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("File")

        file.addAction("Baru")
        file.addAction("Simpan")
        file.addAction("Keluar")

        edit = bar.addMenu("Edit")

        edit.addAction("Undo Typin")
        edit.addAction("Cut")
        edit.addAction("Copy")

        view = bar.addMenu("View")

        view.addAction("Tools Window")
        view.addAction("Type Info")
        view.addAction("Parameter Info")

        help = bar.addMenu("Help")

        help.addAction("Kontak")
        help.addAction("Alamat")

        self.items = QDockWidget("Dockable", self)
        self.listWidget = QListWidget()

        self.listWidget.addItem("File1")
        self.listWidget.addItem("File2")
        self.listWidget.addItem("File3")
        self.listWidget.addItem("File4")
        self.listWidget.addItem("File5")

        self.items.setWidget(self.listWidget)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        self.setLayout(layout)
        self.setWindowTitle("Dock Widget")

def main():
    app = QApplication(sys.argv)
    window = DockWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
