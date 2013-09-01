#!/usr/bin/python

import sys

from PySide.QtGui import *


class CounterWindow(QWidget):

    def __init__(self, parent=None):
        super(CounterWindow, self).__init__(parent)
        self.value = 0
        self.setupUi()

    def setupUi(self):
        self.resize(200, 150)
        self.verticalLayout = QVBoxLayout(self)
        self.push_button = QPushButton("Increment counter", self)
        self.label = QLabel("Counter value: %d" % self.value, self)

        self.verticalLayout.addWidget(self.push_button)
        self.verticalLayout.addWidget(self.label)

        self.push_button.clicked.connect(self.on_push_button)

    def on_push_button(self):
        self.value += 1
        self.label.setText("Counter value: %d" % self.value)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    counter_window = CounterWindow()
    counter_window.show()
    sys.exit(app.exec_())
