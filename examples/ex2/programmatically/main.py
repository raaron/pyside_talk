#!/usr/bin/python

import sys

from PySide.QtGui import *


class ExampleWindow(QWidget):

    def __init__(self, parent=None):
        super(ExampleWindow, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(200, 150)
        self.pushButton = QPushButton("Hide label", self)
        self.pushButton.move(30, 30)
        self.label = QLabel("Label to hide...", self)
        self.label.move(30, 90)

        self.pushButton.clicked.connect(self.label.hide)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    example_window = ExampleWindow()
    example_window.show()
    sys.exit(app.exec_())
