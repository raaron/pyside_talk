#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView

# Create Qt application and the QDeclarative view
app = QApplication(sys.argv)
view = QDeclarativeView('view.qml')
view.show()
sys.exit(app.exec_())
