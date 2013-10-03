#!/usr/bin/env python


from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *

import connection


def createView(title, model):
    window = QWidget()
    window.resize(1300, 400)

    view1 = get_relational_table_view(window)
    view2 = get_table_view_for_table('employee', window)
    view3 = get_table_view_for_table('city', window)
    view4 = get_table_view_for_table('country', window)

    grid = QGridLayout(window)
    grid.addWidget(view1, 1, 0)
    grid.addWidget(view2, 0, 2)
    grid.addWidget(view3, 0, 0)
    grid.addWidget(view4, 0, 1)
    return window

def get_table_view_for_table(name, parent):

    model = QSqlTableModel()
    model.setTable(name)
    model.select()
    view = QTableView(parent)
    view.setModel(model)
    return  view

def get_relational_table_view(parent):
    model = QSqlRelationalTableModel()
    model.setTable("employee")

    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.setRelation(2, QSqlRelation('city', 'id', 'name'))
    model.setRelation(3, QSqlRelation('country', 'id', 'name'))

    model.setHeaderData(1, Qt.Horizontal, "Name")
    model.setHeaderData(2, Qt.Horizontal, "City")
    model.setHeaderData(3, Qt.Horizontal, "Country")

    model.select()
    view = QTableView(parent)
    view.setModel(model)
    view.setItemDelegate(QSqlRelationalDelegate(view))
    return  view



if __name__ == '__main__':

    import sys
    connection.getDbConnection("QMYSQL", "127.0.0.1", "pyzh", "root", "")
    app = QApplication(sys.argv)
    model = QSqlRelationalTableModel()
    view = createView("Relational Table Model", model)
    view.show()
    sys.exit(app.exec_())

