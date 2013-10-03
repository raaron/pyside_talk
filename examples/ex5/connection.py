'''
Handle database connections for many different types of databases.
@author: Aaron Richiger
@contact: a.richi@bluewin.ch
@date: 06.02.2011
'''
from PySide.QtSql import *


def getDbConnection(dbType, hostName, databaseName, userName,
                    password, connectionName=QSqlDatabase.defaultConnection):
    '''
    Get a database connection.
    @param dbType: One of the following database driver types:
        - QDB2
        - QIBASE
        - QMYSQL
        - QOCI
        - QODBC
        - QPSQL
        - QSQLITE
        - QSQLITE2
        - QTDS
    @type dbType: str
    @type all_the_rest: str
    @rtype: QSqlDatabase
    @raise AaDatabaseConnectionError: if connecting to the database fails.
    '''
    db = QSqlDatabase.addDatabase(dbType, connectionName)
    db.setHostName(hostName)
    db.setDatabaseName(databaseName)
    db.setUserName(userName)
    db.setPassword(password)
    db.open()
    if not db.isOpen():
        raise DatabaseConnectionError
    return db


class DatabaseConnectionError(Exception):
    '''
    This exception is raised if there is no open database connection.
    '''
    def __str__(self):
        '''
        String representation of the error.
        @rtype: str
        '''
        return "There is no open database connection."


if __name__ == '__main__':
    dbTranssibira = getDbConnection("QMYSQL", "127.0.0.1", "transsibiria", "transsibirian", "passageist")
