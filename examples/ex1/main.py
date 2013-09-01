#!/usr/bin/python

import sys

from PySide.QtGui import *


if __name__ == '__main__':

    # Create a Qt application
    app = QApplication(sys.argv)

    # Create a Label and show it
    label = QLabel("Hello World")
    label.resize(200, 100)
    label.show()

    # Enter Qt application main loop
    sys.exit(app.exec_())





