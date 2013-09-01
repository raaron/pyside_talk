#!/usr/bin/env python

import sys
import os
import traceback

from PySide.QtGui import *

import controller


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = controller.Controller()
    c.start()
    app.exec_()
